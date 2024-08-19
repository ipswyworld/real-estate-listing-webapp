from django.contrib import admin
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.utils.html import format_html
from .models import (
    CustomUser, UserProfile, Category, Property, PropertyImage, 
    Inquiry, Favorite, Message, Transaction, Review, Report
)
import csv

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1
    readonly_fields = ['preview']

    def preview(self, obj):
        return format_html('<img src="{}" width="100" height="100"/>', obj.real_estate_app_propertyimage_image.url)

    preview.short_description = 'Preview'


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'real_estate_app_property_title', 'real_estate_app_property_category', 
        'real_estate_app_property_price', 'real_estate_app_property_location',
        'thumbnail_preview'
    )
    search_fields = ('real_estate_app_property_title', 'real_estate_app_property_description')
    list_filter = ('real_estate_app_property_category', 'real_estate_app_property_price')
    actions = ['download_property_report', 'export_as_csv']
    inlines = [PropertyImageInline]
    readonly_fields = ['thumbnail_preview']

    def thumbnail_preview(self, obj):
        if obj.real_estate_app_property_thumbnail:
            return format_html('<img src="{}" width="100" height="100"/>', obj.real_estate_app_property_thumbnail.url)
        return "No Thumbnail"

    thumbnail_preview.short_description = 'Thumbnail Preview'

    def download_property_report(self, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="properties_report.pdf"'

        p = canvas.Canvas(response, pagesize=letter)
        p.setFont("Helvetica-Bold", 16)
        p.drawString(100, 750, "Properties Report")

        p.setFont("Helvetica-Bold", 12)
        p.drawString(30, 710, "Title")
        p.drawString(150, 710, "Category")
        p.drawString(270, 710, "Price")
        p.drawString(350, 710, "Location")

        y = 690
        p.setFont("Helvetica", 10)

        for property in queryset:
            p.drawString(30, y, property.real_estate_app_property_title)
            p.drawString(150, y, property.real_estate_app_property_category.real_estate_app_category_name)
            p.drawString(270, y, f"{property.real_estate_app_property_price:.2f}")
            p.drawString(350, y, property.real_estate_app_property_location)
            y -= 20

            if y < 50:
                p.showPage()
                y = 750
                p.setFont("Helvetica", 10)

        p.showPage()
        p.save()

        return response

    download_property_report.short_description = 'Download Property Report (PDF)'

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta}.csv'
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected Properties as CSV"


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('real_estate_app_report_name', 'real_estate_app_report_created_at')
    actions = ['download_pdf']

    def download_pdf(self, request, queryset=None):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        p = canvas.Canvas(response, pagesize=letter)
        p.setFont("Helvetica-Bold", 16)
        p.drawString(100, 750, "System Reports")

        y = 710
        p.setFont("Helvetica", 12)

        for report in queryset:
            p.drawString(30, y, f"Report Name: {report.real_estate_app_report_name}")
            p.drawString(30, y - 20, f"Created At: {report.real_estate_app_report_created_at}")
            p.drawString(30, y - 40, f"Content: {report.real_estate_app_report_content[:100]}...")
            y -= 80

            if y < 50:
                p.showPage()
                y = 750
                p.setFont("Helvetica", 12)

        p.showPage()
        p.save()

        return response

    download_pdf.short_description = 'Download Selected Reports (PDF)'

# Register remaining models
admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Inquiry)
admin.site.register(Favorite)
admin.site.register(Message)
admin.site.register(Transaction)
admin.site.register(Review)
