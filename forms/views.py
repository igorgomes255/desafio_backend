from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UploadForm


def model_form_upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Arquivo salvo com sucesso. Envie para parsear o CNAB!!!"
            )
            return redirect("upload")
    else:
        form = UploadForm()
    return render(request, "upload.html", {"form": form})
