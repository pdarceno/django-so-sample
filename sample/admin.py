from django.contrib import admin

from .models import Issuer
from .models import Offering
from .models import Investment
from .models import Profile

class IssuerAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    list_filter = ('name',)

class OfferingAdmin(admin.ModelAdmin):
    fields = ('offering_name',)
    list_display = ('offering_name',)
    list_filter = ('offering_name',)

class ProfileAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    list_filter = ('name',)

class InvestmentAdmin(admin.ModelAdmin):
    fields = ( 'name',)
    list_display = ('name',)
    list_filter = ('name',)

admin.site.register(Issuer, IssuerAdmin)
admin.site.register(Offering, OfferingAdmin)
admin.site.register(Investment, InvestmentAdmin)
admin.site.register(Profile, ProfileAdmin)