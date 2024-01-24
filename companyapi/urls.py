from django.contrib import admin
from django.urls import path, include
from .views import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#Swagger Settings
schema_view = get_schema_view(
   openapi.Info(
      title="Pizza App Learning API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=[]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page),
    path('api/v1/', include('api.urls')),
    path('', include('vege.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('authentication/', include('authentication.urls')),
    path('orders/', include('orders.urls')),
    path('learning/', include('learning.urls')),
    path('todos/', include('todos.urls')),

   #Swagger Urls
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
