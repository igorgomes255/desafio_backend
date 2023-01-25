from rest_framework.views import APIView, Response, Request, status
from django.shortcuts import render, redirect
from .serializers import CnabFileSerializer
from .forms import UploadForm
from django.http import HttpResponse


class CnabFile(APIView):
    def post(self, request):
        serializer = CnabFileSerializer(data=request.FILES)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


def model_form_upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("cnab")
    else:
        form = UploadForm()
    return render(request, "upload.html", {"form": form})
