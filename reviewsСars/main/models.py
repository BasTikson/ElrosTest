from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=256, unique=True)

class Manufacturers(models.Model):
    name = models.CharField(max_length=256, unique=True)
    country =  models.ForeignKey(Country, on_delete=models.CASCADE, related_name='manufacturers')

class Cars(models.Model):
    name = models.CharField(max_length=256)
    manufacturer = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cars')
    start_year = models.DateField()
    end_year = models.DateField(null=True, blank=True)

class Comments(models.Model):
    email_autor = models.EmailField()
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return f"комментарий  {self.email_autor} о {self.car.name}"


