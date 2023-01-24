from django.shortcuts import render


def cnab(request):
    return render(request, "index.html")
