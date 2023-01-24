from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Transaction
from .serializers import CnabSerializer
from utils.cnab import cnab_parser

import ipdb


class CnabView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"

    def get(self, request: Request) -> Response:
        cnab = Transaction.objects.all()

        serializer = CnabSerializer(cnab, many=True)

        return Response({"cnab": serializer.data})

    def post(self, request: Request) -> Response:
        all_objects = cnab_parser()
        serializer = CnabSerializer(data=all_objects, many=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
