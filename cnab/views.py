from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Transaction
from forms.models import Cnab
from .serializers import CnabSerializer
from utils.cnab import cnab_parser
from django.shortcuts import redirect


class CnabView(APIView):
    def post(self, request: Request) -> Response:
        file_name = Cnab.objects.last().cnab

        all_objects = cnab_parser(str(file_name))
        serializer = CnabSerializer(data=all_objects, many=True)

        serializer.is_valid(raise_exception=True)

        if serializer.is_valid():
            serializer.save()

            return redirect("cnab")
        else:
            return render(request, "upload.html")


class CnabGetView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"

    def get(self, request: Request) -> Response:
        cnab = Transaction.objects.all()

        serializer = CnabSerializer(cnab, many=True)

        return Response({"cnab": serializer.data})
