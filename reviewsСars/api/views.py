from rest_framework import viewsets, permissions, status
from .models import Country, Manufacturers, Cars, Comments
from .serializers.serializers_countrys import  CountrySerializer
from .serializers.serializers_manufacturers import ManufacturersSerializer
from .serializers.serializers_cars import CarsSerializer
from .serializers.serializers_comments import CommentsSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import Country
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from .renderers import CSVStudentDataRenderer, ExcelStudentDataRenderer, CSVStudentDataRendererDetail, ExcelStudentDataRendererDetail


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




class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"], renderer_classes=[CSVStudentDataRenderer, ExcelStudentDataRenderer])
    def download_file(self, request):
        queryset = self.get_queryset()
        now = timezone.now()
        file_name = f"Country_{now:%Y-%m-%d_%H-%M-%S}.{request.accepted_renderer.format}"
        serializer = CountrySerializer(queryset, many=True)
        response = Response(serializer.data, headers={"Content-Disposition": f'attachment; filename="{file_name}"'})
        return response

    @action(detail=True, methods=['get'], renderer_classes=[CSVStudentDataRendererDetail, ExcelStudentDataRendererDetail])
    def download_file_detail(self, request, pk=None):
        queryset = self.get_object()
        now = timezone.now()
        file_name = f"Country_{now:%Y-%m-%d_%H-%M-%S}.{request.accepted_renderer.format}"
        serializer = CountrySerializer(queryset)
        response = Response(serializer.data, headers={"Content-Disposition": f'attachment; filename="{file_name}"'})
        return response


class ManufacturersViewSet(viewsets.ModelViewSet):
    queryset = Manufacturers.objects.all()
    serializer_class = ManufacturersSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"], renderer_classes=[CSVStudentDataRenderer, ExcelStudentDataRenderer])
    def download_file(self, request):
        queryset = self.get_queryset()
        now = timezone.now()
        file_name = f"Country_{now:%Y-%m-%d_%H-%M-%S}.{request.accepted_renderer.format}"
        serializer = ManufacturersSerializer(queryset, many=True)
        response = Response(serializer.data, headers={"Content-Disposition": f'attachment; filename="{file_name}"'})
        return response

class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"], renderer_classes=[CSVStudentDataRenderer, ExcelStudentDataRenderer])
    def download_file(self, request):
        queryset = self.get_queryset()
        now = timezone.now()
        file_name = f"Country_{now:%Y-%m-%d_%H-%M-%S}.{request.accepted_renderer.format}"
        serializer = CarsSerializer(queryset, many=True)
        response = Response(serializer.data, headers={"Content-Disposition": f'attachment; filename="{file_name}"'})
        return response

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedComments]

    @action(detail=False, methods=["get"], renderer_classes=[CSVStudentDataRenderer, ExcelStudentDataRenderer])
    def download_file(self, request):
        queryset = self.get_queryset()
        now = timezone.now()
        file_name = f"Country_{now:%Y-%m-%d_%H-%M-%S}.{request.accepted_renderer.format}"
        serializer = CommentsSerializer(queryset, many=True)
        response = Response(serializer.data, headers={"Content-Disposition": f'attachment; filename="{file_name}"'})
        return response


    @action(detail=True, methods=['get'], renderer_classes=[CSVStudentDataRenderer, ExcelStudentDataRenderer])
    def download_file_detail(self, request, pk=None):
        queryset = self.get_object()
        now = timezone.now()
        file_name = f"Country_{now:%Y-%m-%d_%H-%M-%S}.{request.accepted_renderer.format}"
        serializer = CommentsSerializer(queryset)
        response = Response(serializer.data, headers={"Content-Disposition": f'attachment; filename="{file_name}"'})
        return response


