"""Container_Terminal URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^vessel/', views.vessel),
    url(r'^vessel2/', views.vessel2),
    url(r'^vessel3/', views.vessel3),
    url(r'^part_bay/', views.part_bay),
    url(r'^part_bay2/', views.part_bay2),
    url(r'^bookCont/', views.bookCont),
    url(r'^bay_structure/', views.bay),
    url(r'^createVes/', views.createVes),
    url(r'^createBay/', views.createBay),
    url(r'^Ves/', views.Ves),
    url(r'^bayNo/', views.bayNo),
    url(r'^check_vesName/', views.check_vesName),



    # url(r'^part_bay3/', views.part_bay3),

    # url(r'^haha/',views.haha)

]
