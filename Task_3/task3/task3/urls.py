"""task3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url,include
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teacher/', views.teacher_view),
    path('create/', views.create_view),
    path('home/', views.show_result_view),
    
    
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^delete/(?P<prn>\d*[A-Z a-z])/$', views.delete_view),
    url(r'^update/(?P<prn>\d*[A-Z a-z])/$', views.update_view),
    url(r'^result/', views.show_result_view),
    # url(r'^result/(?P<prn>\d*[A-Z a-z])/$', views.show_result_view),
    
    
]
