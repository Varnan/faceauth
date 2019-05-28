"""faceauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView

import face_app.views as views

urlpatterns = [


    # Admin Console URL
    url(r'^admin/', include(admin.site.urls)),

    # URL For social-auth API's
    url(r'^social-auth/', include('social_django.urls')),

    # User Login Page
    url(r'^login/$', TemplateView.as_view(template_name='login.html'), name='login'),

    # User Logout Operation
    url(r'^logout/$',logout,{'next_page': '/login/'},name='logout'),

    # User Home Page
    url(r'^$', views.home, name='home'),

    #DeAuth Callback
    url(r'^deauthtication/$',views.DeAuthCallback.as_view(), name="deauthtication")



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


