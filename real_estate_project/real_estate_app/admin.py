from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import CustomUser, UserProfile, Category, Property, PropertyImage, Inquiry, Favorite, Message, Transaction, Review, Report

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'location')
    search_fields = ('title', 'description')
    list_filter = ('category', 'price')
    actions = ['download_property_report']
    inlines = [PropertyImageInline]

    def download_property_report(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=properties_report.csv'
        writer = csv.writer(response)
        writer.writerow(['Title', 'Category', 'Price', 'Location', 'Description'])
        properties = queryset.values_list('title', 'category__name', 'price', 'location', 'description')
        for property in properties:
            writer.writerow(property)
        return response

    download_property_report.short_description = 'Download Property Report'

admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Inquiry)
admin.site.register(Favorite)
admin.site.register(Message)
admin.site.register(Transaction)
admin.site.register(Review)
admin.site.register(Report)
