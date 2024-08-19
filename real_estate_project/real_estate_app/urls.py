# real_estate_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('filter_properties/', views.filter_properties, name='filter_properties'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.sign_in, name='sign_in'),
    path('logout/', views.logout_view, name='logout'),
    path('create_listing/', views.create_listing, name='create_listing'),
    path('request_property/', views.request_property, name='request_property'),
    path('properties/', views.property_list, name='property_list'),
    path('properties/<int:property_id>/', views.property_detail, name='property_detail'),
]
