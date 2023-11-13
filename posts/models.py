from django.db import models
from authentication.models import user


# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    subheading = models.CharField(max_length=1000)
    content = models.TextField(max_length=50000)
    image = models.ImageField(upload_to="uploads", null=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
