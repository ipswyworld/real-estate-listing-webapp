# real_estate_project/urls.py

from django.contrib import admin
from django.urls import path, include
from real_estate_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.sign_in, name='signin'),
    path('logout/', views.logout_view, name='logout'),
    path('create_listing/', views.create_listing, name='create_listing'),
    path('properties/<int:property_id>/', views.property_detail, name='property_detail'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('toggle_favorite/<int:property_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('filter_properties/', views.filter_properties, name='filter_properties'),
    path('properties/', views.property_list, name='property_list'),
   
    
    # Include the authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Add this line
]

# Static files and media settings (ensure these are already configured)
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
