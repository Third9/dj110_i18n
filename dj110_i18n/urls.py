from django.conf.urls import include, url
from django.contrib import admin
from django.views.i18n import JavaScriptCatalog
from django.conf.urls.i18n import i18n_patterns
from myapp.views import MyApp

js_info_dict = {
    'packages': ('dj110_i18n')
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    url(r'^$', MyApp.as_view(), name='home'),
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(**js_info_dict), name='javascript-catalog'),
)