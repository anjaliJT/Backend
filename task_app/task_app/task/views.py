from django.shortcuts import render
from djangorestframework import api_view, api_view
# Create your views here.


@api_view(['GET'])
def multiply(request:Request) -> Response:
    