from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from .models import Country, Manufacturers, Cars, Comments

from .serializers.serializers_countrys import CountrySerializer
from .serializers.serializers_manufacturers import ManufacturersSerializer
from .serializers.serializers_cars import CarsSerializer
from .serializers.serializers_comments import CommentsSerializer

class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated


class IsAuthenticatedComments(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'POST':
            return True

        return request.user and request.user.is_authenticated

# ToDo: Реализовать логику авторизации, может быть
# ToDo: Поиграться немного с полями в серелизаторах, чтобы оно не скопом нам все вываливало

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ManufacturersViewSet(viewsets.ModelViewSet):
    queryset = Manufacturers.objects.all()
    serializer_class = ManufacturersSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedComments]


# ToDo: Функционал скачивания при GET запросе в указанном формате.