from django.contrib import admin
from .models import Patient, SkinImage, Diagnosis

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'created_at')
    search_fields = ('name', 'user__username')
    list_filter = ('created_at',)

@admin.register(SkinImage)
class SkinImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'uploaded_at', 'image_thumbnail')
    list_filter = ('uploaded_at',)
    search_fields = ('patient__name',)

    def image_thumbnail(self, obj):
        if obj.image:
            return f"<img src='{obj.image.url}' width='50' height='50' />"
        return "No image"
    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = 'Thumbnail'

@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'get_patient_name', 'image', 'diagnosis_1', 'confidence_1',
        'diagnosis_2', 'confidence_2', 'diagnosis_3', 'confidence_3', 'created_at'
    )
    list_filter = ('created_at',)
    search_fields = ('image__patient__name', 'diagnosis_1', 'diagnosis_2', 'diagnosis_3')

    def get_patient_name(self, obj):
        return obj.image.patient.name
    get_patient_name.short_description = 'Patient'
