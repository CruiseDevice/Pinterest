from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/$',views.image_create,name='create'),
    url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.image_detail,name='detail'),
    url(r'^my_post/$',views.my_post,name='my_post'),
    url(r'^',views.index,name='index'),
    # url(r'^create/$',views.image_create,name='create')
]
