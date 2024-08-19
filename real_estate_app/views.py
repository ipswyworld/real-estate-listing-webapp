# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from urllib.parse import urlencode
from django.http import JsonResponse

from .forms import SignUpForm, PropertyForm, InquiryForm
from .models import Property, Favorite, Message, Report, Review, Transaction

def home(request):
    new_properties = Property.objects.order_by('-real_estate_app_property_id')[:5]
    favorites = Favorite.objects.filter(real_estate_app_favorite_user=request.user) if request.user.is_authenticated else []
    return render(request, 'home.html', {'new_properties': new_properties, 'favorites': favorites})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def create_listing(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.agent = request.user
            property.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = PropertyForm()
    return render(request, 'create_listing.html', {'form': form})

def filter_properties(request):
    sale_rent = request.GET.get('sale_rent')
    location = request.GET.get('location')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    property_type = request.GET.get('property_type')

    query_params = {}
    if sale_rent:
        query_params['sale_rent'] = sale_rent
    if location:
        query_params['location'] = location
    if min_price:
        query_params['min_price'] = min_price
    if max_price:
        query_params['max_price'] = max_price
    if property_type:
        query_params['property_type'] = property_type

    url = reverse('property_list')
    full_url = f"{url}?{urlencode(query_params)}"
    return redirect(full_url)

def property_detail(request, property_id):
    property_obj = get_object_or_404(Property, pk=property_id)
    
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_detail', property_id=property_obj.id)
    else:
        form = InquiryForm(initial={'real_estate_app_inquiry_property': property_obj})
    
    return render(request, 'property_detail.html', {'property': property_obj, 'form': form})

@login_required
def user_dashboard(request):
    messages = Message.objects.filter(real_estate_app_message_receiver=request.user)
    reports = Report.objects.filter(real_estate_app_report_user=request.user)
    reviews = Review.objects.filter(real_estate_app_review_client=request.user)
    transactions = Transaction.objects.filter(real_estate_app_transaction_client=request.user)
    
    context = {
        'messages': messages,
        'reports': reports,
        'reviews': reviews,
        'transactions': transactions,
    }
    return render(request, 'user_dashboard.html', context)

def toggle_favorite(request, property_id):
    property_obj = get_object_or_404(Property, pk=property_id)
    favorite, created = Favorite.objects.get_or_create(
        real_estate_app_favorite_user=request.user,
        real_estate_app_favorite_property=property_obj
    )
    
    if not created:
        favorite.delete()
        return JsonResponse({'status': 'removed'})
    
    return JsonResponse({'status': 'added'})

def property_list(request):
    properties = Property.objects.all()

    # Get filter parameters from request
    sale_rent = request.GET.get('sale_rent')
    location = request.GET.get('location')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    property_type = request.GET.get('property_type')

    # Apply filters to the queryset
    if sale_rent:
        properties = properties.filter(real_estate_app_property_additional_details__icontains=sale_rent)
    if location:
        properties = properties.filter(real_estate_app_property_location__icontains=location)
    if min_price:
        properties = properties.filter(real_estate_app_property_price__gte=min_price)
    if max_price:
        properties = properties.filter(real_estate_app_property_price__lte=max_price)
    if property_type:
        properties = properties.filter(real_estate_app_property_category__real_estate_app_category_name__icontains=property_type)

    return render(request, 'property_list.html', {'properties': properties})