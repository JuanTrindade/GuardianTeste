from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Sum

# MODELS
from . import models

# SERIALIZERS
from . import seriazliers


class ContratosList(APIView):
    @swagger_auto_schema(responses={200: seriazliers.ContratosSerializer(many=True)})
    def get(self, request):
        try:
            contratos = models.Contratos.objects.all()
            contratos_serializer = seriazliers.ContratosSerializer(contratos, many=True)
            
            return Response(
                {'Data': contratos_serializer.data}, 
                status=status.HTTP_200_OK
            )
        
        except TimeoutError as err:
            return Response(
                {'error': str(err)},
                status=status.HTTP_408_REQUEST_TIMEOUT
            )
    
    @swagger_auto_schema(request_body=seriazliers.ContratosSerializer)
    def post(self, request):
        try:
            contrato_serializer = seriazliers.ContratosSerializer(data=request.data)

            if contrato_serializer.is_valid():
                contrato_serializer.save()

                return Response(
                    {'Created': contrato_serializer.data},
                    status=status.HTTP_201_CREATED
                )
            
            return Response(
                contrato_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
        except Exception as err:
            return Response(
                {'error': str(err)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ContratosRead(APIView):
    @swagger_auto_schema(responses={200: seriazliers.ContratosSerializer(many=True)})
    def get(self, request, pk, cpf, data_emissao, estado):
        try:
            contratos = models.Contratos.objects.filter(
                pk=pk, 
                cpf=cpf, 
                data_emissao=data_emissao, 
                estado=estado
            )

            contratos_serializer = seriazliers.ContratosSerializer(contratos, many=True)

            return Response(
                {'Data': contratos_serializer.data},
                status=status.HTTP_200_OK
            )
        
        except TimeoutError as err:
            return Response(
                {'error': str(err)},
                status=status.HTTP_408_REQUEST_TIMEOUT
            )


class ContratosResumo(APIView):
    @swagger_auto_schema(responses={200: seriazliers.ParcelasSerializer(many=True)})
    def get(self, request, cpf, data_emissao, estado):
        try:
            total_a_receber_parcelas = models.Parcelas.objects.filter(
                contrato__cpf=cpf, 
                contrato__data_emissao=data_emissao,
                contrato__estado=estado
            ).aggregate(Sum('valor_parcela'))['valor_parcela__sum']


            numero_contratos_total = models.Contratos.objects.filter(
                cpf=cpf,
                data_emissao=data_emissao,
                estado=estado
            ).count()


            total_desembolsado = models.Contratos.objects.filter(
                cpf=cpf,
                data_emissao=data_emissao,
                estado=estado
            ).aggregate(Sum('valor_desembolsado'))['valor_desembolsado__sum']


            taxa_contratos = models.Contratos.objects.filter(
                cpf=cpf,
                data_emissao=data_emissao,
                estado=estado
            ).aggregate(Sum('taxa_contrato'))['taxa_contrato__sum']


            taxa_media_contratos = taxa_contratos / numero_contratos_total


            data = {
                'total_a_receber_parcelas': total_a_receber_parcelas,
                'total_desembolsado': total_desembolsado,
                'numero_contratos_total': numero_contratos_total,
                'taxa_media_contratos': round(taxa_media_contratos, 2)
            }

            return Response(
                {'Data': data},
                status=status.HTTP_200_OK
            )

        except TimeoutError as err:
            return Response(
                {'error': str(err)},
                status=status.HTTP_408_REQUEST_TIMEOUT
            )


class ParcelaCreate(APIView):
    @swagger_auto_schema(request_body=seriazliers.ParcelasSerializer)
    def post(self, request):
        try:
            parcela_serializer = seriazliers.ParcelasSerializer(data=request.data)
            
            if parcela_serializer.is_valid():
                parcela_serializer.save()

                return Response(
                    {'Created': parcela_serializer.data},
                    status=status.HTTP_201_CREATED
                )

            return Response(
                parcela_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as err:
            return Response(
                {'error': str(err)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )