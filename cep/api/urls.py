from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('ceps/', views.CEPList.as_view(), name='cep-list'),
    path('ceps/<str:pk>/', views.CEPDetail.as_view(), name='cep-detail'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
