from django.db import models
from patient.models import patientModel
from doctor.models import doctorModel,AvailableTimeModel
# Create your models here.
APPOINTMENT_TYPE =[
  ('Online','Online'),
  ('Offline','Offline'),
]

APPOINTMENT_STATUS =[
  ('Pending','Pending'),
  ('Running','Running'),
  ('Completed','Completed'),
]

class AppointmentModel(models.Model):
  patient = models.ForeignKey(patientModel, on_delete=models.CASCADE)
  doctor = models.ForeignKey(doctorModel, on_delete=models.CASCADE)
  appointment_type = models.CharField(max_length=10,choices=APPOINTMENT_TYPE)
  appointment_status = models.CharField(max_length=10,choices=APPOINTMENT_STATUS,default="Pending")
  symptom = models.TextField()
  time = models.OneToOneField(AvailableTimeModel,on_delete=models.CASCADE)
  cancel = models.BooleanField(default=False)
  def __str__(self):
        return f"Doctor : {self.doctor.user.first_name} , Patient : {self.patient.user.first_name}"
