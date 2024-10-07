from rest_framework import serializers
from ..models import Country, Manufacturers, Cars, Comments


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["name"]


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ["name", "start_year", "end_year"]


class ManufacturersSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    cars = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    def get_country(self, obj):
        country = obj.country
        serializer = CountrySerializer(country)
        return serializer.data

    def get_cars(self, obj):
        self.cars = Cars.objects.filter(manufacturer=obj)
        serializers = CarsSerializer(self.cars, many=True)
        return serializers.data

    def get_comments_count(self, obj):
        count_comments = Comments.objects.filter(car__in=self.cars).count()
        return count_comments

    class Meta:
        model = Manufacturers
        fields = '__all__'
