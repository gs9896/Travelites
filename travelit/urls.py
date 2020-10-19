from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('bookings/',views.bookings,name='bookings'),
    path('places/(?P<place>\d+)/)',views.places,name='places'),
]