from django.conf.urls import patterns, url

from kd_agent import views

urlpatterns = patterns('',

    url(r'^api/v1/namespaces/(?P<namespace>[a-zA-Z]{1,10})/pods$',views.get_pod_list),

)