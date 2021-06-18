from django.db import models


class Tutorial(models.Model):
    name = models.CharField(max_length=20,null=False, blank=False, default='')
    pw = models.CharField(max_length=20,null=False,blank=False, default='')