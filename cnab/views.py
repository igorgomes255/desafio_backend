from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Transaction, Cnab
from .serializers import CnabSerializer, CnabFileSerializer
from utils.cnab import cnab_parser


class CnabFile(APIView):
    def post(self, request):
        serializer = CnabFileSerializer(data=request.FILES)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class CnabView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"

    def get(self, request: Request) -> Response:
        cnab = Transaction.objects.all()

        serializer = CnabSerializer(cnab, many=True)

        return Response({"cnab": serializer.data})

    def post(self, request: Request) -> Response:
        file_name = Cnab.objects.all()[0].cnab

        all_objects = cnab_parser(str(file_name))
        serializer = CnabSerializer(data=all_objects, many=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response({"cnab": serializer.data}, status.HTTP_201_CREATED)
