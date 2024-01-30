# banks/models.py
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from users.models import User

class Bank(models.Model):
    id = models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=255)
    routing_number = models.CharField(max_length=20)
    swift_bic = models.CharField(max_length=20)

    def __str__(self):
        return self.bank_name

@receiver(pre_delete, sender=Bank)
def bank_pre_delete(sender, instance, **kwargs):
    # Використовуйте ім'я поля, яке вказує на банк у моделі User
    if User.objects.filter(bank=instance).exists():
        raise ValueError("Неможливо видалити банк, оскільки є пов'язані користувачі.")
