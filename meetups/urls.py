"""meetups URL Configuration

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
from django.urls import path, include

# import settings to access config
from django.conf import settings

# for serving images
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # load all urls from meets app
    path('', include('meets.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# static(<urlpath to serve files at>, document_root=<path to to files on system>)
