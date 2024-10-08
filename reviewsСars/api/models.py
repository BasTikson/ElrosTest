from django.db import models

class Country(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=256, unique=True, db_column='name')

    class Meta:
        db_table = 'Country'

class Manufacturers(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=256, unique=True, db_column='name')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='manufacturers', db_column='country_id')

    class Meta:
        db_table = 'Manufacturers'

class Cars(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=256, db_column='name')
    manufacturer = models.ForeignKey(Manufacturers, on_delete=models.CASCADE, related_name='cars', db_column='manufacturer_id')
    start_year = models.DateField(db_column='start_year')
    end_year = models.DateField(null=True, blank=True, db_column='end_year')

    class Meta:
        db_table = 'Cars'

class Comments(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    email_autor = models.EmailField(db_column='email_autor')
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='comments', db_column='car_id')
    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at')
    comment = models.TextField(db_column='comment')

    def __str__(self):
        return f"комментарий {self.email_autor} о {self.car.name}"

    class Meta:
        db_table = 'Comments'