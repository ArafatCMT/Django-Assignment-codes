from django.db import models
from authors.models import Registration
# Create your models here.
class Transaction(models.Model):
    account = models.ForeignKey(Registration, related_name='transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)

    def __str__(self):
        return f'{self.account.user.email}'