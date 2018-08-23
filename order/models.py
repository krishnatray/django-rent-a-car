from django.db import models
from django.conf import settings
from car.models import Car


class Coupon(models.Model):
    code = models.CharField(max_length=5, blank=True)
    discount = models.IntegerField()
    expired = models.DateTimeField()
    
    class Meta:
        db_table = 'coupon'

    def __str__(self):
        return f'{self.code} expired on {self.expired} - {self.discount}%'

    def save(self, *args, **kwargs):
        from django.utils.crypto import get_random_string
        self.code = get_random_string(5)
        super(Coupon, self).save(*args, **kwargs)


class Order(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.CharField(max_length=20)
    approval = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    total_price = models.IntegerField(null=True, blank=True)
    comment = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='orders')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='orders')

    class Meta:
        db_table = 'order'

    def __str__(self):
        return f'{self.user} rent a {self.car}, {self.start_date} - {self.end_date}'





