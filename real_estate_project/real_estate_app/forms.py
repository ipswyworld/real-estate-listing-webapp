from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Category, Property, PropertyImage, Client, Inquiry, Transaction, Review, Report

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
        fields = ['image']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = '__all__'

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
        fields = ('username', 'email', 'user_type', 'phone_number', 'agree_terms')

class SignInForm(AuthenticationForm):
    pass
