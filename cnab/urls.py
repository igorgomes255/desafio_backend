from django.urls import path
from . import views

urlpatterns = [
    path("transactions/", views.CnabView.as_view(), name="transactions"),
    path("cnab/", views.CnabGetView.as_view(), name="cnab"),
]
