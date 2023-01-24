from django.shortcuts import render

import ipdb


def cnab(request):
    return render(request, "index.html")
