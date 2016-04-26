from django.contrib import admin

from .models import Cause, CauseCategory, MedicalResponsibility, ReasonHospitalized, DiagnosisCode


admin.site.register(Cause)
admin.site.register(CauseCategory)
admin.site.register(DiagnosisCode)
admin.site.register(MedicalResponsibility)
admin.site.register(ReasonHospitalized)
