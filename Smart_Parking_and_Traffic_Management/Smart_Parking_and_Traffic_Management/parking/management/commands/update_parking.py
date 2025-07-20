from django.core.management.base import BaseCommand
from parking.models import ParkingSlot
import time
import random

class Command(BaseCommand):
    help = "Simulate real-time sensor data updates"

    def handle(self, *args, **kwargs):
        while True:
            slots = ParkingSlot.objects.all()
            for slot in slots:
                slot.status = random.choice(["available", "occupied"])
                slot.save()
                self.stdout.write(self.style.SUCCESS(f"Updated {slot.slot_number} to {slot.status}"))
            time.sleep(5)  # Update every 5 seconds
