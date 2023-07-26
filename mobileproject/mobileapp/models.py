from django.db import models

# Create your models here.
class Mobile(models.Model):
    model_name=models.CharField(max_length=250)
    price=models.CharField(max_length=250)
    desc = models.TextField()
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.model_name
