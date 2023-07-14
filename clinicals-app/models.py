from django.db import models

# Create your models here.
class Patient(models.Model):
    lastname=models.CharField(max_length=20)
    firstname=models.CharField(max_length=20)
    age=models.IntegerField()

CHOICES=[('hw','Height/Weight'),('bp','Blood Pressure'),('heartrate','HeartRate')]
class ClinicalData(models.Model):
    componentName=models.CharField(max_length=20,choices=CHOICES)
    componenetValue=models.CharField(max_length=20)
    measuredDatetime=models.DateTimeField(auto_now_add=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
