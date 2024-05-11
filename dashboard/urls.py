from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_with_pivot, name = 'dashboard_with_pivot'),
    path('data', views.pivote_data, name = 'pivot_data'),
]