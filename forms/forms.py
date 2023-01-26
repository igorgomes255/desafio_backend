from django import forms
from .models import Cnab


class UploadForm(forms.ModelForm):
    class Meta:
        model = Cnab
        fields = "__all__"
