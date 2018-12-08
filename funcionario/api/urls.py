from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('funcionarios/', views.FuncionarioList.as_view(), name='funcionario-list'),
    path('funcionarios/<pk>/', views.FuncionarioDetail.as_view(), name='funcionario-detail'),
    path('', views.api_root, name='api-root'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
