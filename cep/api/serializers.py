from rest_framework import serializers
from .models import CEP


class CEPSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CEP
        fields = ('cep', 'logradouro', 'bairro', 'localidade', 'uf', 'url')
