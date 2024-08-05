from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.email

class AppUsage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=100)
    click_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user.email} - {self.device_id}"

class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100, primary_key=True)
    transaction_date = models.DateTimeField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.email} - {self.transaction_id}"

