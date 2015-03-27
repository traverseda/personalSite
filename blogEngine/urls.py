from django.conf.urls import patterns, include, url
from blogEngine.views import postView, getUrlFromSlug, postList

urlpatterns = patterns('',
    url(r'^post/(?P<pk>\d*)/(?P<slug>.*)/$', postView),
    url(r'^post/(?P<pk>\d*)/$', postView),
    url(r'^post/(.*)/$', getUrlFromSlug)
)
