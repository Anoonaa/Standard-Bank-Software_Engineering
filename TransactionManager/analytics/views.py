from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.timezone import now, timedelta
from .models import User, AppUsage, Transactions
from .serializers import UserSerializer, AppUsageSerializer, TransactionsSerializer

class UserTransactionsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        user_data = UserSerializer(user).data

        last_30_days = now() - timedelta(days=30)
        transactions = Transactions.objects.filter(user=user, transaction_date__gte=last_30_days)
        transactions_data = TransactionsSerializer(transactions, many=True).data

        app_usage = AppUsage.objects.filter(user=user, click_time__gte=last_30_days)
        total_time_spent = app_usage.count()

        data = {
            'first_name': user_data['first_name'],
            'transactions': transactions_data,
            'total_time_spent': total_time_spent
        }

        return Response(data)

