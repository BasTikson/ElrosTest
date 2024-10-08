from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, ManufacturersViewSet, CarsViewSet, CommentsViewSet

router = DefaultRouter()
router.register(r'countries', CountryViewSet, basename='country')
router.register(r'manufacturers', ManufacturersViewSet, basename='manufacture')
router.register(r'cars', CarsViewSet, basename='car')
router.register(r'comments', CommentsViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]