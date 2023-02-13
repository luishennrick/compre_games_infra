from django.db import models

class Produto(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    score = models.IntegerField()
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name