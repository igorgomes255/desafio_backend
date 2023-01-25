from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.CnabFile.as_view()),
    path("upload/form/", views.model_form_upload, name=""),
]
