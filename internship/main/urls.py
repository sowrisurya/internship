from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('seller_login/', views.sellerlogin),
    path('user_login/', views.userlogin),
    path('hospital_login/', views.hospitallogin),
    path('bloodbank_login/', views.bloodbanklogin),
    path('clinic_login/', views.cliniclogin),
    path('diagnostic_login/', views.diagnosticlogin),
]
