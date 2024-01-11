from django.db import models
from django.contrib.auth.models import User
from patient.models import patientModel
# Create your models here.
class DesignationModel(models.Model):
  name = models.CharField(max_length=30)
  slug = models.SlugField(max_length=40)
  def __str__(self):
      return self.name


class SpecialisationModel(models.Model):
  name = models.CharField(max_length=30)
  slug = models.SlugField(max_length=40)

  def __str__(self):
      return self.name


class AvailableTimeModel(models.Model):
  name = models.CharField(max_length=50)
  def __str__(self):
      return self.name


class doctorModel(models.Model):
   user = models.OneToOneField(User,on_delete=models.CASCADE)
   designation = models.ManyToManyField(DesignationModel)
   specialisation = models.ManyToManyField(SpecialisationModel)
   availAbleTime = models.ManyToManyField(AvailableTimeModel)
   image = models.ImageField(upload_to="doctor/images")
   fee = models.IntegerField()
   meet_link = models.CharField(max_length = 100)

   def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

STAR_RATTING =[
  ('⭐','⭐'),
  ('⭐⭐','⭐⭐'),
  ('⭐⭐⭐','⭐⭐⭐'),
  ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
  ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
]

class reviewModel(models.Model):
  reviewer = models.ForeignKey(patientModel,on_delete=models.CASCADE)
    # reviewer = models.ForeignKey(Patient,on_delete=models.CASCADE)
  doctor = models.ForeignKey(doctorModel,on_delete=models.CASCADE)
  body = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  ratting = models.CharField(choices=STAR_RATTING, max_length=10)

  def __str__(self):
        return f"{self.reviewer.user.first_name} {self.reviewer.user.last_name}"
