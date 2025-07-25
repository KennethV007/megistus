from django.urls import path
from . import views
 
urlpatterns = [
    # Health and info endpoints
    path('health/', views.health_check, name='health_check'),
    path('info/', views.api_info, name='api_info'),
    path('example/', views.example_endpoint, name='example_endpoint'),
    
    # Transaction endpoints
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/<int:transaction_id>/', views.transaction_detail, name='transaction_detail'),
    path('transactions/demo/', views.demo_transactions, name='demo_transactions'),
] 