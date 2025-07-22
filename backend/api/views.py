from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


@api_view(['GET'])
def health_check(request):
    """Simple health check endpoint"""
    return Response({
        'status': 'healthy',
        'message': 'Megistus backend is running!',
        'version': '1.0.0'
    })


@api_view(['GET'])
def api_info(request):
    """API information endpoint"""
    return Response({
        'name': 'Megistus API',
        'version': '1.0.0',
        'description': 'Django REST API for Megistus application',
        'endpoints': {
            'health': '/api/health/',
            'info': '/api/info/',
        }
    })


@api_view(['GET', 'POST'])
def example_endpoint(request):
    """Example endpoint demonstrating GET and POST"""
    if request.method == 'GET':
        return Response({
            'message': 'This is a GET request',
            'data': ['item1', 'item2', 'item3']
        })
    elif request.method == 'POST':
        data = request.data
        return Response({
            'message': 'Received POST data',
            'received_data': data,
            'status': 'success'
        }, status=status.HTTP_201_CREATED)
