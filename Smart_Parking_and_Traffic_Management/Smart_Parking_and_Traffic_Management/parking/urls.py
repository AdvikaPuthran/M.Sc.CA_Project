from django.urls import path
from . import views

urlpatterns = [
    #  UI Pages (Render HTML)
    path('parking-slots/', views.parking_slots_page, name='parking_slots_page'),
    path('traffic-status/', views.traffic_status_page, name='traffic_status_page'),
    path('reservation/', views.parking_reservation_page, name='parking_reservation_page'),
    path('payment/', views.payment_page, name='payment_page'),
    path('reserve-all/', views.reserve_all_slots, name='reserve_all_slots'),
    path('reservation_success/', views.reservation_success, name='reservation_success'),
    path('about_us_page/', views.about_us, name='about_us_page'),

    #  API Endpoints (Return JSON)
    path('api/parking-slots/', views.parking_slots_api, name='parking_slots_api'),
    path('api/traffic-status/', views.get_traffic_status, name='traffic_status'),
    path('api/reservation/', views.get_parking_reservation_data, name='get_parking_reservation_data'),
    path('api/available-slots/', views.get_available_slots, name='available_slots'),
    path('api/parking-data/', views.get_parking_data, name='get_parking_data'),

    #  Reservation & Payment APIs
    path('api/payment/', views.process_payment, name='process_payment'),
    path('api/reserve/', views.reserve_parking_slot, name='reserve_parking_slot'),
    path('api/confirm-reservation/', views.confirm_reservation, name='confirm_reservation'),
]
