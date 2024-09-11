from django.contrib import admin
from .models import GymTip, NutritionTip, ContactRequest

admin.site.register(GymTip)
admin.site.register(NutritionTip)
admin.site.register(ContactRequest)
