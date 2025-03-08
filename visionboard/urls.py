from visionboard import views
from django.urls import path

urlpatterns = [
    path('create/', views.CreatingVision, name = 'CreatingVision'),
    path('visions/', views.Visions, name = 'Visions')
]