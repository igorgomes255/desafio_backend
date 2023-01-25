from django.db import models


class Cnab(models.Model):
    cnab = models.FileField(upload_to="./uploads/")
