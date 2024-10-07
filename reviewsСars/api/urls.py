from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, ManufacturersViewSet, CarsViewSet, CommentsViewSet

router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'manufacturers', ManufacturersViewSet)
router.register(r'cars', CarsViewSet)
router.register(r'comments', CommentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('export/', export_data, name='export_data'),
]