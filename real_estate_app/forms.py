# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Category, Property, PropertyImage, Inquiry, Transaction, Review, Report

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = ['real_estate_app_propertyimage_image'] 

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['real_estate_app_inquiry_property', 'real_estate_app_inquiry_client', 'real_estate_app_inquiry_date']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'real_estate_app_customuser_type', 'real_estate_app_customuser_phone_number', 'real_estate_app_customuser_agree_terms')

class SignInForm(AuthenticationForm):
    pass
