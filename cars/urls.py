from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:id>/', views.DetailCarView.as_view(), name='details'),
    path('buy_now/<int:id>/', views.buy_now, name='buy_now'),
]