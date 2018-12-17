from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('homepage', views.homepage, name='homepage'),
    url('get_status', views.get_status, name='get_status'),
    # url('station_codes', views.station, name='station_codes'),
    url('seat_availability', views.seat_availability, name='seat_availability'),
    url(r'^seats', views.seatAvailability, name='seatAvailability'),
    url('train_fare', views.train_fare, name='train_fare'),
    url(r'^liveStatus$', views.liveStatus , name='liveStatus'),
    url(r'^pnr_status$', views.pnr_status, name='pnr_status'),
    url(r'^pnrStatus$', views.pnrStatus, name='pnrStatus'),
]