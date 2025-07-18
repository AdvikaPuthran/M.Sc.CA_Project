from django.db import models
from django.utils import timezone
import pytz

class CustomerEnquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        db_table = "customer_enquiry"  # This ensures the correct table name

    def __str__(self):
        return self.name
    
    def get_created_at_ist(self):
        """Convert UTC time to IST when displaying"""
        ist = pytz.timezone('Asia/Kolkata')
        return timezone.localtime(self.created_at, ist)
