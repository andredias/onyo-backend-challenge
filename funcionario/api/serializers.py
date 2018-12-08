from rest_framework import serializers
from .models import Funcionario


class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Funcionario
        fields = ('cpf', 'nome', 'cep', 'logradouro', 'numero', 'complemento',
                  'bairro', 'localidade', 'uf', 'url')
        read_only_fields = ('logradouro', 'bairro', 'localidade', 'uf')
