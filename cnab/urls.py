from django.urls import path
from . import views

urlpatterns = [
    path("cnab/", views.CnabView.as_view()),
    path("upload/", views.CnabFile.as_view()),
]
