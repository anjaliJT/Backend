from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, generics, status 
from rest_framework.decorators import action
from .models import Event, Reservation
from .serializers import EventSerializer, ReservationSerializer
from rest_framework.views import APIView
from django.db import transaction 
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.db.models import Sum, Q, F
from django.db.models.functions import Coalesce 
# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all() 

        status_param = self.request.query_params.get('status')
        venue_param = self.request.query_params.get('venue')
        if status_param: 
            queryset = queryset.filter(status=status_param)
        
        if venue_param:
            queryset = queryset.filter(venue__icontains=venue_param)
        
        queryset =  queryset.annotate(reserved_seats=Coalesce(
            Sum(
                'reservations__seats_reserved',
                filter=Q(reservations__status='confirmed'),                
            ),
            0
        ), 
        available_seats = F('total_seats') - F('reserved_seats')
        ) 

        return queryset

# **ReservationViewSet — filter by event_id, custom cancel action**
class ReservationViewSet(viewsets.ModelViewSet): 
    serializer_class = ReservationSerializer

    def get_queryset(self):
        queryset = Reservation.objects.all() 

        event_id = self.request.query_params.get('event_id')

        if event_id: 
            queryset = queryset.filter(event_id=event_id)
        
        return queryset

    def create(self, request, *args, **kwargs):
        event_id = request.data.get('event')
        seats_requested = request.data.get('seats_reserved')
        
        with transaction.atomic():
            event = Event.objects.select_for_update().get(id=event_id)
            
            total_reserved = event.reservations.filter(status='confirmed').aggregate(
                total=Sum('seats_reserved')
            )['total'] or 0
            
            available_seats = event.total_seats - total_reserved
            
            if seats_requested > available_seats:
                return Response({'error': f'Only {available_seats} seats available'}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            reservation = serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['post'])
    def cancel(self,request,pk=None):
        reservation = self.get_object() 

        if reservation.status == 'cancelled': 
            return Response({'error': 'Already cancelled.'}, status=400)

        reservation.status = 'cancelled'
        reservation.save() 

        return Response(self.get_serializer(reservation).data)


# ----- my own practice for  different views. -------- 


# class EventListApiView(generics.ListAPIView):
#     queryset = Event.objects.all() 
#     serializer_class = EventSerializer
   
# class EventDetailAPIView(generics.RetrieveAPIView): 
#     queryset = Event.objects.all() 
#     serialzer = EventSerializer

# class EventCreatAPIView(generics.CreateAPIView):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer

# class ReservationListApiView(generics.ListAPIView): 
#     queryset = Reservation.objects.all() 
#     serializer_class = ReservationSerializer

# class ReservationCreateAPIView(APIView):
#     def post(self,request): 
#         event_id = request.data.get('event')
#         seats_requested  = int(request.data.get('seats_reserved'))

#         with transaction.atomic(): 
#             event = Event.objects.select_for_update().get(id=event_id)
            
#             total_researved = sum(
#                 event.reservations.filter(status='confirmed').values_list('seats_reserved', flat=True))
            
#             available_seats = event.total_seats - total_researved

#             if seats_requested > available_seats: 
#                 return Response(
#                     {
#                         "error" : "Not enough seats available"
#                     },
#                     status = status.HTTP_400_BAD_REQUEST
#                 ) 
            
#             reservation = Reservation.objects.create(
#                 event = event, 
#                 attendee_name = request.data.get("attendee_name"),
#                 attandee_email = request.data.get("attendee_email"),
#                 seats_reserved = seats_requested
#             )

#         return Response({"message": "Reservation successful"})
            
            


# class CancelReservationApiView(APIView): 
#     def patch(self,request,pk): 
#         reservation = get_object_or_404(Reservation, pk=pk)
#         if reservation.event.date < timezone.now().date():
#             return Response(
#                 {"error":  "cannot cancel reservation for past events"}, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         reservation.status =  'cancelled'
#         reservation.save(update_fields=["status"])

#         return self.response(
#             {"message": "Reservation cancelled successfully"},
#             status = status.HTTP_200_OK
#         )