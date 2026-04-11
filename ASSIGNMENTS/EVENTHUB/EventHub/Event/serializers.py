"""
Computed Field : 
reservation count using serializermethod

validate available_seats >!total_seats.
serializer,  python queryset into json format. 
"""

from rest_framework import serializers
from .models import Reservation, Event

class EventSerializer(serializers.ModelSerializer): 
    # Two Custom Behaviours
    reservation_count = serializers.SerializerMethodField() 
    available_seats = serializers.IntegerField(read_only=True)


    # Adds a read-only field to the API response
    # value is calculated dynamically(not stored in DB)


    class Meta : 
        model = Event 

        fields = '__all__'
    
    def get_reservation_count(self,obj):
        return obj.reservations.filter(status='confirmed').count()         

class ReservationSerializer(serializers.ModelSerializer): 
    class Meta : 
        model = Reservation 
        fields = ['id', 'event', 'attendee_name', 'attendee_email',
        'seats_reserved', 'status', 'created_at']
        read_only_fields = ['status', 'created_at']

    def validate_seats_reserved(self,value):
        if value < 1: 
            raise serializers.ValidationError('Must reserve at least 1 seat.')
        return value
        

    




