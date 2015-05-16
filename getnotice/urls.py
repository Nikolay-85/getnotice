from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from notices import views

urlpatterns = staticfiles_urlpatterns()

urlpatterns += patterns('',
    (r'^$', TemplateView.as_view(template_name="dashboard.html")),
    url(r'^messages/$', views.MessageApi.as_view(), name='messages_api'),
)

