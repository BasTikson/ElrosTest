from rest_framework import viewsets, permissions, status
from .models import Country, Manufacturers, Cars, Comments
from .serializers.serializers_countrys import  CountrySerializer
from .serializers.serializers_manufacturers import ManufacturersSerializer
from .serializers.serializers_cars import CarsSerializer
from .serializers.serializers_comments import CommentsSerializer
import csv
from io import StringIO
from openpyxl import Workbook
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import Country

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

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

    @action(detail=False, methods=['GET'])
    def download_file(self, request):
        # Получаем параметр format из запроса
        file_format = request.query_params.get('format', 'csv').lower()

        # Получаем все объекты Country
        countries = self.get_queryset()
        # Сериализуем данные
        serializer = self.get_serializer(countries, many=True)
        data = serializer.data


        if file_format == 'csv':
            # Создаем CSV файл в памяти
            csv_buffer = StringIO()
            writer = csv.writer(csv_buffer)

            # Заголовки CSV файла
            header = data[0].keys() if data else []
            writer.writerow(header)

            # Записываем данные в CSV файл
            for item in data:
                writer.writerow(item.values())

            # Возвращаем CSV файл в ответе
            response = Response(csv_buffer.getvalue(), content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="countries.csv"'
            return response

        elif file_format == 'xlsx':
            # Создаем XLSX файл в памяти
            workbook = Workbook()
            sheet = workbook.active

            # Заголовки XLSX файла
            header = data[0].keys() if data else []
            sheet.append(header)

            # Записываем данные в XLSX файл
            for item in data:
                sheet.append(item.values())

            # Возвращаем XLSX файл в ответе
            xlsx_buffer = StringIO()
            workbook.save(xlsx_buffer)
            xlsx_buffer.seek(0)

            response = Response(xlsx_buffer.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="countries.xlsx"'
            return response

        else:
            return Response({'error': 'Unsupported file format'}, status=400)


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