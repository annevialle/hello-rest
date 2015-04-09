from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from helloRest import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'v1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/(?P<pk>[0-9]+)/$', views.HelloDetail.as_view()),
    url(r'^box/(?P<sender>[0-9]+)/(?P<receiver>[0-9]+)/spin/$', views.activate_box),
    url(r'^box/(?P<pk>[0-9]+)/nospin/$', views.deactivate_box),
    url(r'^box/(?P<pk>[A-Za-z0-9]+)/detail/$', views.BoxDetail.as_view()),
    url(r'^box/(?P<pk>[A-Za-z0-9]+)/$', views.spin_box),

]
