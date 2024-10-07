from rest_framework import serializers
from ..models import Country, Manufacturers


class ManufacturersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturers
        fields = ["name"]


class CountrySerializer(serializers.ModelSerializer):
    manufacturers = serializers.SerializerMethodField()

    def get_manufacturers(self, obj):
        manufacturers = Manufacturers.objects.filter(country=obj)
        serializer = ManufacturersSerializer(manufacturers, many=True)
        return serializer.data

    class Meta:
        model = Country
        fields = '__all__'
