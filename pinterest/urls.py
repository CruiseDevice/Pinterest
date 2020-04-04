from django.conf.urls import url

from . import views

app_name="pinterest"

urlpatterns = [
    url(r'^create/$',views.image_create,name='create'),
    url(r'^like_image/$', views.like_image, name='like_image'),
    url(r'^delete/(?P<id>\d+)/$', views.delete_image, name='delete_image'),
    url(r'^my_post/$',views.my_post, name='my_post'),
    url(r'^',views.index,name='index'),
]
