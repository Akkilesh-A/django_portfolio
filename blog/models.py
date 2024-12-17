from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    date=models.DateField()
    image=models.ImageField(upload_to='blogs/images/',default="none")