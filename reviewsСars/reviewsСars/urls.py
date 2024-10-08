from django.contrib import admin
from django.urls import path, include
from .views import Login, Menu

urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    path('menu/', Menu.as_view(), name="menu"),
    path('api/', include("api.urls")),
    path('admin/', admin.site.urls),

]

