from django.conf.urls import include, url
from django.views.generic.base import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
   url(r'', include('boundaries.urls')),
   url(r'', include('imago.urls')),
   url(r'^admin/', include(admin.site.urls)),
]
