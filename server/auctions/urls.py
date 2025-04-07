from django.urls import path
from . import views

urlpatterns = [
    path('auction/<int:auction_id>/', views.auction_detail, name='auction_detail'),
]