from django.urls import path
from app import views

urlpatterns = [
    path('display/<slug:Name>',views.display, name="disp"),
]

