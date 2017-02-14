from django.conf.urls import include, url
from django.contrib import admin
from myapp.views import MyApp

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^$', MyApp.as_view(), name='home'),
]
