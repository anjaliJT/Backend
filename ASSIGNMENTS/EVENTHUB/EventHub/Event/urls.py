from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    EventViewSet,ReservationViewSet)

router = DefaultRouter()
router.register(r'events',       EventViewSet,       basename='event')

router.register(r'reservations', ReservationViewSet, basename='reservation')
urlpatterns = router.urls

#---my own practic----
# urlpatterns = [
    
#     path('events/list', EventListApiView.as_view(), name='event-list'),
#     path('events/', EventCreatAPIView.as_view(), name='event-list'),
#     path('events/<int:pk>/',EventDetailAPIView.as_view(), name='event-details'),

#     # Reservation APIs
#     path('reservations/', ReservationCreateAPIView.as_view(), name='reservation-create'),
#     path('reservations/list', ReservationListApiView.as_view(), name='reservation'),
#     path('reservations/<int:pk>/cancel/',CancelReservationApiView.as_view())
#     # path('reservations/', ReservationListApiView)
# ]

