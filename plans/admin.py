from django.contrib import admin

from .models import FitnessPlan,FitnessBlog, Customer,Blog,Food,Health,Love,Beauty,Culture

admin.site.register(FitnessPlan)
admin.site.register(Customer)
admin.site.register(Blog)
admin.site.register(Health)
admin.site.register(Love)
admin.site.register(Beauty)
admin.site.register(Food)
admin.site.register(Culture)
admin.site.register(FitnessBlog)