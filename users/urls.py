from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('success/', views.home, name='success'),
]


#twilio
# 17P2NYJK9D436Z6T1EQE6L36

#sendrid
# 2N5UYG6QDGKQ5GM4EAY9555L