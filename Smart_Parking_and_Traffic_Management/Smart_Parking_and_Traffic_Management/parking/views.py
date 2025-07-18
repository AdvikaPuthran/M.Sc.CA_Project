from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_datetime
from django.utils import timezone
import json
import random
from datetime import datetime
from .models import ParkingSlot, TrafficStatus, ParkingReservation, Payment


#  Render Parking Availability Page
def parking_slots_page(request):
    return render(request, 'parking/parking_slots.html')

#  Render Traffic Status Page
def traffic_status_page(request):
    return render(request, 'parking/traffic_status.html')

#  Render Parking Reservation Page
def parking_reservation_page(request):
    return render(request, 'parking/parking_reservation.html')

def about_us(request):
    return render(request, 'parking/about_us.html')

#  Get real-time Traffic Status
def get_traffic_status(request):
    city = request.GET.get('city', "").strip()
    location = request.GET.get('location', "").strip()

    if not city or not location:
        return JsonResponse({"error": "Please provide both city and location!"}, status=400)

    traffic = TrafficStatus.objects.filter(city__icontains=city, location__icontains=location).first()

    if traffic:
        traffic.congestion_level = random.randint(1, 10)  # Simulate congestion updates
        traffic.save()
        congestion_text = "Low" if traffic.congestion_level < 4 else "Medium" if traffic.congestion_level < 7 else "High"

        return JsonResponse({
            "traffic_data": [{
                "city": traffic.city,
                "location": traffic.location,
                "congestion_level": congestion_text
            }]
        })

    return JsonResponse({"traffic_data": []})  # No data found

#  API: Get Available Parking Slots (City & Location included)
def get_available_slots(request):
    city = request.GET.get('city', "").strip()
    location = request.GET.get('location', "").strip()

    slots = ParkingSlot.objects.filter(status="Available", city__icontains=city)

    if location:
        slots = slots.filter(location__icontains=location)

    slots_data = list(slots.values('slot_number', 'location', 'city', 'status'))

    return JsonResponse({"slots": slots_data})

#  API: Fetch Parking Reservation Data
def get_parking_reservation_data(request):
    city = request.GET.get('city', "").strip()
    location = request.GET.get('location', "").strip()
    date = request.GET.get('date', datetime.today().strftime('%Y-%m-%d'))

    reservations = ParkingReservation.objects.filter(city__icontains=city, start_time__date=date)
    if location:
        reservations = reservations.filter(location__icontains=location)

    data = {
        "city": city,
        "date": date,
        "reserved_slots": reservations.count(),
        "available_slots": ParkingSlot.objects.filter(status="Available", city__icontains=city).count(),
        "reservations": list(reservations.values('slot_number', 'location', 'start_time', 'end_time'))
    }

    return JsonResponse(data)

#  API: Reserve a Parking Slot
@csrf_exempt
def reserve_parking_slot(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            slot_number = data.get('slot_number')
            start_time = data.get('start_time')
            end_time = data.get('end_time')

            if not slot_number or not start_time or not end_time:
                return JsonResponse({'error': 'Missing required fields'}, status=400)

            # Convert string timestamps to datetime
            start_time = timezone.datetime.fromisoformat(start_time)
            end_time = timezone.datetime.fromisoformat(end_time)

            #  Fetch the ParkingSlot instance
            try:
                slot_instance = ParkingSlot.objects.get(slot_number=slot_number)
            except ParkingSlot.DoesNotExist:
                return JsonResponse({'error': 'Slot not found'}, status=404)

            #  Insert using slot_number_id
            reservation = ParkingReservation(
                slot_number_id=slot_instance.slot_number,  #  Use slot_number_id explicitly
                city=slot_instance.city,
                location=slot_instance.location,
                start_time=start_time,
                end_time=end_time,
            )
            reservation.save()

            return JsonResponse({'success': True, 'message': 'Reservation successful'})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

#  API: Fetch All Parking Slots (City & Location included)
def parking_slots_api(request):
    city = request.GET.get('city', '')  # Get city from request
    location = request.GET.get('location', '')  # Get location filter

    # Filter parking slots by city and location
    slots = ParkingSlot.objects.filter(city__icontains=city, location__icontains=location)

    # Count available & occupied slots
    available_slots = slots.filter(status="Available").count()
    occupied_slots = slots.filter(status="Occupied").count()

    slots_data = list(slots.values('slot_number', 'location', 'status'))  # Convert QuerySet to list

    response_data = {
        "message": "Parking data retrieved successfully",
        "available_slots": available_slots,
        "occupied_slots": occupied_slots,
        "parking_slots": slots_data  #  Ensure this key exists
    }

    return JsonResponse(response_data)

#  API: Confirm Payment & Reservation
@csrf_exempt
def confirm_reservation(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            slot_number = data.get("slot_number")
            start_time = timezone.datetime.fromisoformat(data.get("start_time"))
            end_time = timezone.datetime.fromisoformat(data.get("end_time"))

            if not (slot_number and start_time and end_time):
                return JsonResponse({"message": "Missing required fields", "status": "error"}, status=400)

            # Update slot status after payment
            slot = get_object_or_404(ParkingSlot, slot_number=slot_number)
            slot.status = "Occupied"
            slot.save()

            return JsonResponse({"message": "Reservation confirmed!", "status": "success"})

        except Exception as e:
            return JsonResponse({"message": str(e), "status": "error"}, status=500)

    return JsonResponse({"message": "Invalid request", "status": "error"}, status=400)

@csrf_exempt  # Only use this if you are testing without CSRF token
def payment_page(request):
    slot_number = request.GET.get('slot')
    location = request.GET.get('location')
    city = request.GET.get('city')
    start_time = request.GET.get('start')
    end_time = request.GET.get('end')

    if request.method == "POST":
        # Get payment details from form
        account_number = request.POST.get("account_number")
        payment_method = request.POST.get("payment_method")
        amount = request.POST.get("amount")

        # Save reservation to database
        ParkingReservation.objects.create(
            slot_number=slot_number,
            city=city,
            location=location,
            start_time=start_time,
            end_time=end_time,
            payment_method=payment_method,
            account_number=account_number,
            amount=amount,
            status="Confirmed"
        )

        return redirect("reservation_success")  # Redirect to success page

    return render(request, "parking/payment.html", {
        "slot_number": slot_number,
        "location": location,
        "city": city,
        "start_time": start_time,
        "end_time": end_time
    })


@csrf_exempt
def process_payment(request):
    if request.method == "POST":
        data = json.loads(request.body)

        account_number = data.get("account_number")
        payment_method = data.get("payment_method")  # optional
        amount = data.get("amount")  # optional

        if not account_number:
            return JsonResponse({"success": False, "message": "Account number is required."}, status=400)

        # Create Payment object with status 'Completed'
        payment = Payment.objects.create(
            account_number=account_number,
            status="Completed"  # You can simulate failure for testing too
        )

        return JsonResponse({
            "success": True,
            "message": "Payment successful.",
            "payment_id": payment.id
        })
    return JsonResponse({"success": False, "message": "Invalid request method."}, status=405)


@csrf_exempt
def reserve_parking_slot(request):
    if request.method == "POST":
        data = json.loads(request.body)

        slot_number = data.get("slot_number")
        start_time = parse_datetime(data.get("start_time"))
        end_time = parse_datetime(data.get("end_time"))
        payment_id = data.get("payment_id")

        if not all([slot_number, start_time, end_time, payment_id]):
            return JsonResponse({"success": False, "message": "Missing required fields."}, status=400)

        try:
            payment = Payment.objects.get(id=payment_id)
        except Payment.DoesNotExist:
            return JsonResponse({"success": False, "message": "Invalid payment ID."}, status=404)

        # Create Reservation
        reservation = ParkingReservation.objects.create(
            slot_number=slot_number,
            start_time=start_time,
            end_time=end_time,
            status="Confirmed",  # Automatically confirmed after successful payment
            payment=payment
        )

        return JsonResponse({
            "success": True,
            "message": "Reservation successful!",
            "reservation_id": reservation.id
        })

    return JsonResponse({"success": False, "message": "Invalid request method."}, status=405)

def get_parking_data(request):
    city = request.GET.get('city', "").strip()
    location = request.GET.get('location', "").strip()

    slots = ParkingSlot.objects.filter(city__icontains=city)

    if location:
        slots = slots.filter(location__icontains=location)

    # Ensure status is either "Available" or "Occupied"
    for slot in slots:
        if slot.status not in ["Available", "Occupied"]:
            slot.status = "Available" if random.choice([True, False]) else "Occupied"
            slot.save()

    data = {
        "parking_slots": list(slots.values('slot_number', 'location', 'status', 'city')),
        "available_slots": slots.filter(status="Available").count(),
        "occupied_slots": slots.filter(status="Occupied").count(),
    }

    return JsonResponse(data)


def reservation_success(request):
    return render(request, "parking/reservation_success.html")


def reserve_all_slots(request):
    if request.method == "POST":  # Ensure it's triggered via a POST request
        available_slots = ParkingSlot.objects.filter(status="Available")

        if not available_slots.exists():
            return JsonResponse({"message": "No available parking slots"}, status=400)

        # Create reservation objects
        reservations = [
            ParkingReservation(
                slot_number=slot,  # Pass the ParkingSlot instance
                city="Mumbai",
                location=slot.location,
                start_time=timezone.now(),
                end_time=timezone.now() + timezone.timedelta(hours=2),
                payment_method="PayPal",
                account_number="345657489233",
                amount=100.0,
                status="Confirmed"
            )
            for slot in available_slots
        ]

        # Bulk insert all reservations
        ParkingReservation.objects.bulk_create(reservations)

        return JsonResponse({"message": f"{len(reservations)} reservations created successfully!"})

    return JsonResponse({"error": "Invalid request method"}, status=405)
