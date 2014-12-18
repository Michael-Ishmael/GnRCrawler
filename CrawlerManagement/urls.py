from django.conf.urls import patterns, url

from CrawlerManagement import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^uploadcompanyfile', views.upload_file, name='fileupload'),
                       url(r'^findcompanywebsite/(\w+)', views.find_company_website, name='findcompanywebsite'),
                       url(r'^findcompanylinks/$', views.find_company_links, name='findcompanylinks'),

)