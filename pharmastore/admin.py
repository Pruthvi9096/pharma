from django.contrib import admin
from .models import Pharmacy,DrugRequest

class pharmacyAdmin(admin.ModelAdmin):
    raw_id_fields =  ('user',)

admin.site.register(Pharmacy,pharmacyAdmin)
admin.site.register(DrugRequest)
