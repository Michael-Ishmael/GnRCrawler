from django.conf.urls import patterns, url

from CrawlerManagement import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index')
)



