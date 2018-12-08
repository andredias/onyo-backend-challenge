import json
from requests import get
from django.conf import settings
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Funcionario
from .serializers import FuncionarioSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'funcionarios': reverse('funcionario-list', request=request, format=format),
    })


def _perform_create_or_update(serializer):
    data = serializer.validated_data
    response = get('{}{}/'.format(settings.CEP_URL, data['cep']))
    if response.status_code != 200:
        data = json.loads(response.content)
        data['detail'] = 'CEP: ' + data['detail']
        raise serializers.ValidationError(data)
    endereco = json.loads(response.content)
    endereco.pop('url')
    data.update(endereco)
    serializer.save()
    return


class FuncionarioList(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

    def perform_create(self, serializer):
        _perform_create_or_update(serializer)
        return


class FuncionarioDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

    def perform_update(self, serializer):
        _perform_create_or_update(serializer)
        return
