from django.contrib import admin
from django.urls import path, include
from .views import LoginView, ApiInteractionView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('api-interaction/', ApiInteractionView.as_view(), name='api_interaction'),
    path('api/', include("api.urls")),
    path('admin/', admin.site.urls),

]
