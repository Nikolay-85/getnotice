from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = staticfiles_urlpatterns()

urlpatterns += patterns('',
    (r'^$', TemplateView.as_view(template_name="dashboard.html")),
)

