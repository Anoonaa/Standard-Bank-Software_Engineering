from rest_framework import serializers
from .models import User, AppUsage, Transactions

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name']

class AppUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUsage
        fields = ['click_time']

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ['transaction_id', 'transaction_date', 'status']

