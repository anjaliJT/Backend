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
    
    # def get_available_seats(self,obj):
    #     total_reserved = obj.reservations.filter(status='confirmed').aggregate(total=models.Sum('seats_reserved'))['total'] or 0
    #     return obj.total_seats - total_reserved
    

    def validate(self,data):
        if data.get('available-seats',0)> data.get('total_seats',0):
            raise serializers.ValidationError('avaiable_seats cannot exceed total  seats')

        return data         

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
        
        def validate(self,data): 
            event = data.get('event')
            if event.status not in ('upcoming', 'ongoing'):
                raise serializers.ValidationError(f"cannot reserve seats for a {event.status} event.")
        
            if data.get('seats_reserved',0)> event.available_seats:
                raise serializers.ValidationError(f"Only {event.available_seats} seat(s) availabe")
            
            return data 
        
        def create(self, validated_data): 
            event = validated_data['event']

            event.available_seats -= validated_data['seats_reserved']
            return Reservation.objects.create(**validated_data)
        

    




