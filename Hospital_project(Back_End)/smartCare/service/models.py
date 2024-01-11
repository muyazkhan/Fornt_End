from django.db import models

# Create your models here.
class serviceModel(models.Model):
  title = models.CharField(max_length=30)
  details = models.TextField()
  image = models.ImageField(upload_to="service/images")
  def __str__(self):
      return self.title
