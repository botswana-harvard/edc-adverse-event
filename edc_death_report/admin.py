from django.contrib import admin

from .models import Cause, CauseCategory, MedicalResponsibility, ReasonHospitalized


admin.site.register(Cause)
admin.site.register(CauseCategory)
admin.site.register(MedicalResponsibility)
admin.site.register(ReasonHospitalized)
