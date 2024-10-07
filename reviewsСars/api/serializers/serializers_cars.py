from rest_framework import serializers
from ..models import Manufacturers, Cars, Comments


class ManufacturersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturers
        fields = ["name"]


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ["email_autor", "created_at", "comment"]


class CarsSerializer(serializers.ModelSerializer):
    manufacturers = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    count_comments = serializers.SerializerMethodField()

    def get_manufacturers(self, obj):
        manufacturer = obj.manufacturer
        serializer = ManufacturersSerializer(manufacturer)
        return serializer.data

    def get_comments(self, obj):
        self.comments = Comments.objects.filter(car=obj)
        serializer = CommentsSerializer(self.comments, many=True)
        return serializer.data

    def get_count_comments(self, obj):
        return self.comments.count()

    class Meta:
        model = Cars
        fields = "__all__"