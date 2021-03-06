"""MyOwnLibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

from accounts.admin import CustomUserAdmin
from accounts.models import CustomUser
from viewer.admin import BookAdmin, AuthorAdmin, GenreAdmin
from viewer.models import Book, Author, Genre
from viewer.views import HomeView

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(CustomUser, CustomUserAdmin)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name='index'),
    path('views/', include('viewer.urls')),
]
