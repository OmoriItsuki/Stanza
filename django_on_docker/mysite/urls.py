"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# made by yasunaga kyohei
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView  
from app import views
import posts

urlpatterns = [
    path('posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
    # path('users/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', posts.views.index, name='home'),
    path('create_account', views.SignUpView.as_view(), name='create_account')
]
