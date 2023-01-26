from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Transaction
from forms.models import Cnab
from .serializers import CnabSerializer
from utils.cnab import cnab_parser
from django.shortcuts import redirect
from django.contrib import messages


class CnabView(APIView):
    def post(self, request: Request) -> Response:
        try:
            file_name = Cnab.objects.last().cnab

            all_objects = cnab_parser(str(file_name))
            serializer = CnabSerializer(data=all_objects, many=True)

            serializer.is_valid(raise_exception=True)

            if serializer.is_valid():
                serializer.save()

                return redirect("cnab")
        except:
            messages.error(request, "Mande o arquivo novamente por favor")
            return render(request, "transaction.html")


class CnabGetView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"

    def get(self, request: Request) -> Response:
        transactions = {}
        negative_transactions = [2, 3, 9]

        cnab = Transaction.objects.values_list("name_shop", "value", "type")

        for owner in cnab:
            transactions[owner[0]] = 0

        for owner in cnab:
            transactions[owner[0]] = (
                transactions[owner[0]] + owner[1]
                if owner[2] not in negative_transactions
                else transactions[owner[0]] - owner[1]
            )

        return Response({"cnab": transactions})
