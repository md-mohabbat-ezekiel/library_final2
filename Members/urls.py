from django.urls import path
from . views import RegistrationFormView,UserLoginView,logOut
urlpatterns = [
    path('register/',RegistrationFormView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',logOut,name='logout')
]
