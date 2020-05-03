"""VersionLog_platform URL Configuration

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
#from VersionInfo.views import say_hello
from VersionInfo.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('hello/', say_hello), #当url指向hello时，去VersionInfo.views调用say_hello的方法
    path('index/', index),
    path('', index)

]
