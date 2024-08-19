# models.py

import os
import logging
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('individual', 'Individual'),
        ('agent', 'Agent'),
        ('developer', 'Developer'),
    )
    real_estate_app_customuser_type = models.CharField(max_length=20, choices=USER_TYPES, default='individual')
    real_estate_app_customuser_phone_number = models.CharField(max_length=15, blank=True, null=True)
    real_estate_app_customuser_agree_terms = models.BooleanField(default=False)
    real_estate_app_client_name = models.CharField(max_length=255, blank=True, null=True)
    real_estate_app_client_email = models.EmailField(unique=True, blank=True, null=True)

class UserProfile(models.Model):
    real_estate_app_userprofile_id = models.AutoField(primary_key=True)
    real_estate_app_userprofile_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    real_estate_app_userprofile_user_type = models.CharField(max_length=20, choices=CustomUser.USER_TYPES)
    real_estate_app_userprofile_phone = models.CharField(max_length=15, blank=True, null=True)
    real_estate_app_userprofile_address = models.CharField(max_length=255, blank=True, null=True)

class Category(models.Model):
    real_estate_app_category_id = models.AutoField(primary_key=True)
    real_estate_app_category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.real_estate_app_category_name

class Property(models.Model):
    real_estate_app_property_id = models.AutoField(primary_key=True)
    real_estate_app_property_title = models.CharField(max_length=100)
    real_estate_app_property_description = models.TextField(default='No description provided')
    real_estate_app_property_price = models.DecimalField(max_digits=10, decimal_places=2)
    real_estate_app_property_location = models.CharField(max_length=100)
    real_estate_app_property_street = models.CharField(max_length=255, blank=True, null=True)
    real_estate_app_property_city = models.CharField(max_length=100, blank=True, null=True)
    real_estate_app_property_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    real_estate_app_property_additional_details = models.TextField(blank=True, null=True)
    real_estate_app_property_agent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='properties', default=1)
    real_estate_app_property_thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Property, self).save(*args, **kwargs)
        if not self.real_estate_app_property_thumbnail and self.images.exists():
            logger.debug("No thumbnail found, creating one.")
            self.create_thumbnail()

    def create_thumbnail(self):
        if not self.images.exists():
            logger.debug("No images found in create_thumbnail method.")
            return

        image_path = self.images.first().real_estate_app_propertyimage_image.path
        thumb_dir = os.path.join(settings.MEDIA_ROOT, 'thumbnails')
        thumb_path = os.path.join(thumb_dir, os.path.basename(image_path))

        os.makedirs(thumb_dir, exist_ok=True)

        try:
            with Image.open(image_path) as img:
                img.thumbnail((250, 167))
                img.save(thumb_path, img.format)
                logger.debug(f"Thumbnail created at {thumb_path}")
                self.real_estate_app_property_thumbnail = os.path.join('thumbnails', os.path.basename(image_path))
                super(Property, self).save()
        except Exception as e:
            logger.error(f"Error creating thumbnail: {e}")

    def __str__(self):
        return self.real_estate_app_property_title

class PropertyImage(models.Model):
    real_estate_app_propertyimage_id = models.AutoField(primary_key=True)
    real_estate_app_propertyimage_property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    real_estate_app_propertyimage_image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"Image for {self.real_estate_app_propertyimage_property.real_estate_app_property_title}"

class Inquiry(models.Model):
    real_estate_app_inquiry_id = models.AutoField(primary_key=True)
    real_estate_app_inquiry_property = models.ForeignKey(Property, on_delete=models.CASCADE)
    real_estate_app_inquiry_client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    real_estate_app_inquiry_date = models.DateField()

class Transaction(models.Model):
    real_estate_app_transaction_id = models.AutoField(primary_key=True)
    real_estate_app_transaction_property = models.ForeignKey(Property, on_delete=models.CASCADE)
    real_estate_app_transaction_client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    real_estate_app_transaction_date = models.DateField()
    real_estate_app_transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)

class Review(models.Model):
    real_estate_app_review_id = models.AutoField(primary_key=True)
    real_estate_app_review_property = models.ForeignKey(Property, on_delete=models.CASCADE)
    real_estate_app_review_client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    real_estate_app_review_text = models.TextField()
    real_estate_app_review_date = models.DateField()

class Report(models.Model):
    real_estate_app_report_id = models.AutoField(primary_key=True)
    real_estate_app_report_name = models.CharField(max_length=255)
    real_estate_app_report_content = models.TextField()
    real_estate_app_report_created_at = models.DateTimeField(auto_now_add=True)

class Favorite(models.Model):
    real_estate_app_favorite_id = models.AutoField(primary_key=True)
    real_estate_app_favorite_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    real_estate_app_favorite_property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='favorites')
    real_estate_app_favorite_created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    real_estate_app_message_id = models.AutoField(primary_key=True)
    real_estate_app_message_sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    real_estate_app_message_receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages')
    real_estate_app_message_subject = models.CharField(max_length=255)
    real_estate_app_message_body = models.TextField()
    real_estate_app_message_sent_at = models.DateTimeField(auto_now_add=True)
    real_estate_app_message_read = models.BooleanField(default=False)
