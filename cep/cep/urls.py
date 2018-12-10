from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='CEP API')

urlpatterns = [
    path('', schema_view),
    path('api/v1/', include('api.urls')),
    path('auth/', include('rest_framework.urls')),
]
