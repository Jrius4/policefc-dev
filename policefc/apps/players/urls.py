from django.urls import path
from apps.players import views

urlpatterns = [
    path('api/players/', views.PlayerListCreate.as_view()),
]