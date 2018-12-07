from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import CEP
from .serializers import CEPSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'ceps': reverse('cep-list', request=request, format=format),
    })


class CEPList(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = CEP.objects.all()
    serializer_class = CEPSerializer


class CEPDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = CEP.objects.all()
    serializer_class = CEPSerializer
