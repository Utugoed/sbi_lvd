from django.contrib import admin

from organisations.models import Organisation


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'address', 'postcode']
    list_filter = ['address', 'postcode']
    search_fields = ['id', 'title']
