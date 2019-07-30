"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', one, name="home"),
    path('about/', about, name="about"),
    path('project/', project, name="project"),
    path('testimonial/', testimonial, name="testimonial"),
    path('blog/', blog, name="blog"),
    path('add/', add, name="add"),
    path('new/', new, name="new"),
    path('delete/<int:id>',delete, name="delete"),
    path('edit/<int:id>',edit, name="edit"),
    path('signup/', signup, name="signup"),
    path('table/', table, name="signupsave"),
    path('delet/<int:id>',delet, name="delete"),
    path('edi/<int:id>',edi, name="edit"),
    path('', login, name="login"),
    path('otp/', otp, name="otp"),
    path('image_upload/', hotel_image_view, name='image_upload'),
    path('success/', success, name='success'),
    path('hotel_images/', display_hotel_images, name = 'hotel_images'),
    path('logout/', logout, name = 'logout'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)