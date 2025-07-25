from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.contrib.auth.models import User

# Import our Transaction model and serializer
from .models import Transaction
from .serializers import TransactionSerializer, TransactionListSerializer


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
            'transactions': '/api/transactions/',
        }
    })


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def transaction_list(request):
    """
    List all transactions for the current user (GET) or create a new transaction (POST).
    """
    if request.method == 'GET':
        # Get all transactions for the current user
        transactions = Transaction.objects.filter(user=request.user).order_by('-transaction_date')
        serializer = TransactionListSerializer(transactions, many=True)
        
        return Response({
            'count': transactions.count(),
            'transactions': serializer.data
        })
    
    elif request.method == 'POST':
        # Create a new transaction
        serializer = TransactionSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            # The serializer will automatically set the user from the request
            transaction = serializer.save()
            return Response(
                TransactionSerializer(transaction).data, 
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {'errors': serializer.errors}, 
                status=status.HTTP_400_BAD_REQUEST
            )


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def transaction_detail(request, transaction_id):
    """
    Retrieve, update, or delete a specific transaction.
    """
    try:
        # Ensure user can only access their own transactions
        transaction = Transaction.objects.get(id=transaction_id, user=request.user)
    except Transaction.DoesNotExist:
        return Response(
            {'error': 'Transaction not found'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    if request.method == 'GET':
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TransactionSerializer(transaction, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def demo_transactions(request):
    """
    Demo endpoint that returns sample transaction data (no authentication required).
    This is useful for testing the frontend before implementing full authentication.
    """
    sample_transactions = [
        {
            'id': 1,
            'username': 'demo_user',
            'amount': '25.50',
            'category': 'gaming',
            'merchant': 'Steam Store',
            'description': 'Purchased new indie game',
            'transaction_date': '2025-01-20T15:30:00Z',
            'is_recurring': False
        },
        {
            'id': 2,
            'username': 'demo_user', 
            'amount': '89.99',
            'category': 'food',
            'merchant': 'Local Restaurant',
            'description': 'Dinner with friends',
            'transaction_date': '2025-01-19T19:45:00Z',
            'is_recurring': False
        },
        {
            'id': 3,
            'username': 'demo_user',
            'amount': '12.99',
            'category': 'utilities',
            'merchant': 'Netflix',
            'description': 'Monthly subscription',
            'transaction_date': '2025-01-15T10:00:00Z',
            'is_recurring': True
        }
    ]
    
    return Response({
        'count': len(sample_transactions),
        'transactions': sample_transactions
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
