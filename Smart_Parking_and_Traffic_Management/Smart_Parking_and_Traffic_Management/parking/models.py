from django.db import models
from django.utils.timezone import now
from datetime import timedelta
from django.utils import timezone

class ParkingSlot(models.Model):
    slot_number = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Occupied', 'Occupied'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Available')  # Fix this!

    class Meta:
        db_table = "parking_slot" 
    

class TrafficStatus(models.Model):
    city = models.CharField(max_length=100, default="Unknown")  # New column
    location = models.CharField(max_length=100)
    congestion_level = models.IntegerField()

    class Meta:
        db_table = "traffic_status" 


    def __str__(self):
        return f"{self.city} - {self.location} - Congestion {self.congestion_level}"


class ParkingReservation(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]

    slot_number = models.CharField(max_length=20)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    # Link to Payment (set in /api/reserve/)
    payment = models.OneToOneField('Payment', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Reservation for Slot {self.slot_number} - {self.status}"

    class Meta:
        db_table = "parking_reservation"


class Payment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ]

    account_number = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment ID {self.id} - {self.status}"

    class Meta:
        db_table = "payment"  # ✅ Custom table name
    
    

