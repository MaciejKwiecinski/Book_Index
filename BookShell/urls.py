"""BookShell URL Configuration

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
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from BookIndex.API.views import DocsView, BookApiView
from BookIndex.views import AddGoogleBookView, index

router = routers.DefaultRouter(trailing_slash=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('db/', AddGoogleBookView.as_view(), name='google_book'),
    path('api/', DocsView.as_view(), name='list'),
    path('api/books/', BookApiView.as_view(), name='book'),
]

urlpatterns += router.urls
