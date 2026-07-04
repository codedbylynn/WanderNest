
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', views.home, name='home'),

    path('about/', views.about, name='about'),

    path('destinations/', views.destinations, name='destinations'),

    path('contact/', views.contact, name='contact'),

]
