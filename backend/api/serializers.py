from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for Transaction model to convert to/from JSON for API endpoints.
    """
    # Read-only field to show username instead of user ID
    username = serializers.CharField(source='user.username', read_only=True)
    
    # Optional: Make user field write-only since we'll set it from the request
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Transaction
        fields = [
            'id',
            'user',
            'username',
            'amount',
            'category', 
            'merchant',
            'description',
            'transaction_date',
            'is_recurring'
        ]
        read_only_fields = ['id', 'username']
    
    def validate_amount(self, value):
        """
        Validate that amount is positive.
        """
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than 0")
        return value
    
    def validate_category(self, value):
        """
        Validate category and convert to lowercase for consistency.
        """
        if not value.strip():
            raise serializers.ValidationError("Category cannot be empty")
        return value.strip().lower()
    
    def validate_merchant(self, value):
        """
        Validate merchant name.
        """
        if not value.strip():
            raise serializers.ValidationError("Merchant cannot be empty")
        return value.strip()

class TransactionListSerializer(TransactionSerializer):
    """
    Simplified serializer for listing transactions (excludes some fields for performance).
    """
    class Meta(TransactionSerializer.Meta):
        fields = [
            'id',
            'username',
            'amount',
            'category',
            'merchant', 
            'transaction_date',
            'is_recurring'
        ] 