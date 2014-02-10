from django.conf.urls import patterns, url

from comics.views import CatalogView

urlpatterns = patterns('',
    url(r'^$', CatalogView.as_view(), name='catalog'),
)
