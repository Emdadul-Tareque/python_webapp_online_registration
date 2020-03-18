from django.db import models


class registration(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)

