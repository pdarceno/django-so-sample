from django.contrib import admin

from .models import Issuer
from .models import Offering
from .models import Investment
from .models import Profile

from decouple import config
from django.utils.html import format_html

class IssuerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Information', {'fields': [
            'name',]}),
    ]
    list_display = ('name',)
    list_filter = ('name',)

class OfferingAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Select Issuer', {'fields': [
        'issuer',]}),
        ('Offering Information', {'fields': [
            'offering_name',]}),
        ('Send Notes', {'fields': [
            'notes',
            'send_notes']}),
    ]

    readonly_fields = ('send_notes',)

    list_display = ('offering_name',)
    list_filter = ('offering_name',)

    def send_notes(self, request):
        url = (config('base_url') + "send-notes/")
        return format_html('<a href="{}" class="button">Send Notes</a>',url)
    send_notes.short_description = 'Send Notes'

class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Select User', {'fields': [
        'user',]}),
        ('Personal Information', {'fields': [
            'name',]}),
    ]
    list_display = ('name',)
    list_filter = ('name',)

class InvestmentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Select Profile', {'fields': [
        'profile',]}),
        ('Investment Information', {'fields': [
            'amount',]}),
    ]
    list_display = ('amount',)
    list_filter = ('amount',)

admin.site.register(Issuer, IssuerAdmin)
admin.site.register(Offering, OfferingAdmin)
admin.site.register(Investment, InvestmentAdmin)
admin.site.register(Profile, ProfileAdmin)