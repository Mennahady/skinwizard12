from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class SkinImage(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='skin_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.patient.name} at {self.uploaded_at}"

class Diagnosis(models.Model):
    image = models.ForeignKey(SkinImage, on_delete=models.CASCADE, related_name='diagnoses')
    diagnosis_1 = models.CharField(max_length=100)
    confidence_1 = models.FloatField()  # e.g., 90% for diagnosis_1
    diagnosis_2 = models.CharField(max_length=100)
    confidence_2 = models.FloatField()
    diagnosis_3 = models.CharField(max_length=100)
    confidence_3 = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Diagnosis for {self.image.patient.name}"