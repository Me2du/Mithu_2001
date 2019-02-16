from django.db import models

# Create your models here.
class mithu_2001model(models.Model):
    F_name=models.CharField(max_length=50)
    L_name=models.CharField(max_length=50)

    def __str__(self):
        return self.F_name

    def __str__(self):
        return self.L_name