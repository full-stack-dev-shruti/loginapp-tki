"""loginapp URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/mysite')),
    path('mysite/', include("mysite.urls")),
    path('admin/', admin.site.urls),
]
