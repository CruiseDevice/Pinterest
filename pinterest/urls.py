from django.conf.urls import url

from . import views

app_name="pinterest"

urlpatterns = [
    url(r'^create/$',views.image_create,name='create'),
    url(r'^delete/(?P<id>\d+)/$', views.delete_image, name='delete_image'),
    url(r'^my_post/$',views.my_post, name='my_post'),
    url(r'^',views.index,name='index'),
]
