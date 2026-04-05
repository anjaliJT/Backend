from django.db import models

# Create your models here.
"""
TO Create : Ticketing Platform : 
user can 
1. Browse Event 
2. Reserve Seats
3. Cancel Reservation

situation to handle : 
last available ticket book by two user at the same time.

"""


class Event( models.Model): 
    Status_Choices = [ 
        ('upcoming', "Upcoming"),
        ('ongoing',"Ongoing"),
        ('completed',"completed"),
    ]

    title = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    date = models.DateField()
    total_seats = models.PositiveIntegerField()
    status =  models.CharField(max_length=10,choices=Status_Choices, default="upcoming")
    created_at = models.DateTimeField(auto_now_add = True )

    def __str___(self): 
        return f"{self.title} at {self.venue}"
    
    class Meta: 
        ordering = ['date']


class Reservation(models.Model): 
    STATUS_CHOICES = [
        ('confirmed',"Confirmed"),
        ('cancelled',"Cancelled"),
    ]

    event = models.ForeignKey(Event,on_delete=models.PROTECT, related_name = 'reservations')
    attendee_name = models.CharField(max_length=200)
    attendee_email = models.EmailField()
    seats_reserved = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="confirmed")
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self): 
        return f"{self.attendee_name} = {self.event.title} ({self.seat_researved}) seats"
    
    class Meta:
        ordering = ['-created_at']

        
