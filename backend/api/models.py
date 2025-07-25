from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

# Create your models here.

class Transaction(models.Model):
    """
    Model representing a financial transaction.
    """
    # User who made the transaction
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='transactions',
        help_text="User who made this transaction"
    )
    
    # Transaction details
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        help_text="Transaction amount in dollars"
    )
    
    category = models.CharField(
        max_length=100,
        help_text="Spending category (e.g., gaming, food, utilities)"
    )
    
    merchant = models.CharField(
        max_length=200,
        help_text="Store or service where transaction occurred"
    )
    
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Optional notes about the transaction"
    )
    
    # Transaction date
    transaction_date = models.DateTimeField(
        help_text="When the transaction actually occurred"
    )
    
    # Optional fields for future features
    is_recurring = models.BooleanField(
        default=False,
        help_text="Whether this is a recurring transaction"
    )
    
    class Meta:
        ordering = ['-transaction_date']  # Most recent first
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
    
    def __str__(self):
        return f"{self.user.username} - ${self.amount} at {self.merchant} ({self.category})"
    
    @property
    def amount_cents(self):
        """Return amount in cents for precise calculations"""
        return int(self.amount * 100)
    
    def save(self, *args, **kwargs):
        # Set transaction_date to current time if not provided
        if not self.transaction_date:
            from django.utils import timezone
            self.transaction_date = timezone.now()
        super().save(*args, **kwargs)
