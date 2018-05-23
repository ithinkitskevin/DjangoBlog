from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'blog'

urlpatterns = [
    # /music/
    url(r'^$',views.IndexView.as_view(), name='index'),
    #Default page, as carrot (^) is the start position and $ is the end position

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # () will group everything together, so 712 will NOT be 7 and 1 and 2
    # THIS IS REGULAR EXPRESSION. So, [0-9] is any integers and [0-9]+ means any two or more digit integer
    url(r'topic/add/$',views.TopicCreate.as_view(), name='topicAdd'),
    url(r'topic/(?P<pk>[0-9]+)/$',views.TopicUpdate.as_view(), name='topicUpdate'),
    url(r'topic/(?P<pk>[0-9]+)/delete/$',views.TopicDelete.as_view(), name='topicDelete'),

    url(r'topic/add/response/$', views.ResponseCreate.as_view(), name='responseAdd'),
    url(r'topic/response/(?P<pk>[0-9]+)/$', views.ResponseUpdate.as_view(), name='responseUpdate'),
    url(r'topic/response/(?P<pk>[0-9]+)/delete/$', views.ResponseDelete.as_view(), name='responseDelete'),
]
