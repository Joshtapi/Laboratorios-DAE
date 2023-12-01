import statistics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models.query_utils import Q
from .models import Vehiculo, VehiculoDocumento
from .serializers import VehiculoSerializer, VehiculoDocumentoSerializer
from rest_framework import status
class TblVehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class TblVehiculoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = VehiculoDocumento.objects.all()
    serializer_class = VehiculoDocumentoSerializer



class SearchVehiculoView(APIView):

    def get(self,request,search):
        matches = Vehiculo.objects.filter(
                Q(placa=search) |
                Q(marca=search) |
                Q(modelo=search)
            )
            
        """ if(matches.count() ==0):

            matches = Vehiculo.objects.all()
         """

        #paginator = MediumSetPagination()
        # results = paginator.paginate_queryset(matches, request)
        serializer = VehiculoSerializer(matches, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)