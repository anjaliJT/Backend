from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer

from django.contrib.auth import authenticate
from django.db import transaction
from django.db.models import Q
from .models import KBEntry, QueryLog
from .serializers import KBEntrySerializer

from django.db.models import Count
from .permissions import IsAdminUser


class UsageSummaryView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        total_queries = QueryLog.objects.aggregate(total=Count('id'))['total']

        active_companies = QueryLog.objects.values('company').distinct().count()

        top_terms = QueryLog.objects.values('search_term') \
            .annotate(count=Count('id')) \
            .order_by('-count')[:5]

        return Response({
            "total_queries": total_queries,
            "active_companies": active_companies,
            "top_search_terms": list(top_terms)
        })

class KBQueryView(APIView):

    def post(self, request):
        search = request.data.get('search')

        if not search:
            return Response({"error": "Search field required"}, status=400)

        company = request.user.company

        with transaction.atomic():
            queryset = KBEntry.objects.filter(
                Q(question__icontains=search) |
                Q(answer__icontains=search)
            )

            count = queryset.count()

            QueryLog.objects.create(
                company=company,
                search_term=search,
                results_count=count
            )

        serializer = KBEntrySerializer(queryset, many=True)

        return Response({
            "search": search,
            "count": count,
            "results": serializer.data
        })

class LoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password')
        )

        if not user:
            return Response({"error": "Invalid credentials"}, status=401)

        token = RefreshToken.for_user(user)
        company = user.company

        return Response({
            "access": str(token.access_token),
            "company_name": company.company_name,
            "api_key": company.api_key
        })
    
class RegisterView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        if User.objects.filter(username=serializer.validated_data['username']).exists():
            return Response({"error": "Username already exists"}, status=400)

        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
            email=serializer.validated_data['email']
        )

        company = user.company
        company.company_name = serializer.validated_data['company_name']
        company.save()

        token = RefreshToken.for_user(user)

        return Response({
            "username": user.username,
            "company_name": company.company_name,
            "api_key": company.api_key,
            "access": str(token.access_token)
        }, status=201)