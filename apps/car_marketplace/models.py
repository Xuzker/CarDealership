from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    is_sold = models.BooleanField(default=False)

    class Meta:
        app_label = 'car_marketplace'
    def __str__(self):
        return f'{self.brand}\t{self.model}\t{self.year}'
