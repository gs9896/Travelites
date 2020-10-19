from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.signUp,name='signup'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('index/',views.index,name='index'), 
]