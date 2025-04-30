from django.contrib import admin
from .models import PatientForm, Doctor, ChatMessage

@admin.register(PatientForm)
class PatientFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'date_of_birth', 'gender', 'duration', 'submitted_date')
    list_filter = ('gender', 'duration', 'condition_frequency', 'affected_body_parts')
    search_fields = ('patient__name', 'name', 'other_conditions')
    
    def submitted_date(self, obj):
        return obj._state.db  # Optional: replace if you add submitted_at field
    submitted_date.short_description = 'Submitted At'

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'email', 'phone_number')
    search_fields = ('name', 'specialty', 'email')

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'sent_at', 'is_from_patient', 'short_message')
    list_filter = ('is_from_patient', 'sent_at')
    search_fields = ('message', 'patient__name', 'doctor__name')

    def short_message(self, obj):
        return obj.message[:50] + ("..." if len(obj.message) > 50 else "")
    short_message.short_description = 'Message'
