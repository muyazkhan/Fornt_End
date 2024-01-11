from django.contrib import admin
from .models import SpecialisationModel,DesignationModel,AvailableTimeModel,doctorModel,reviewModel
# Register your models here.
class specializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
admin.site.register(SpecialisationModel,specializationAdmin)

class designationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
admin.site.register(DesignationModel,designationAdmin)
admin.site.register(AvailableTimeModel)
admin.site.register(doctorModel)
admin.site.register(reviewModel)