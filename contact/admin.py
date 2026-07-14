from django.contrib import admin

# Register your models here.
from .models import Contact
class ContactAdmin(admin.ModelAdmin):
    list_display=["id","name","age"]
    search_fields=["name"]
    ordering=["-name"]
    list_display_links=["name"]
    list_editable=["age"]
    list_filter=["age"]
    list_per_page=10
    readonly_fields=["id"]
    empty_value_display= "N/A"
admin.site.register(Contact,ContactAdmin)