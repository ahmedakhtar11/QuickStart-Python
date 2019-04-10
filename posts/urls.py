# Posts App URLs ==>

from django.conf.urls import url


from django.contrib import admin
from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [

    path('admin/', admin.site.urls),
    url(r'^test1/$', views.test1, name='test1'),
    url(r'^test2/$', views.test2, name='test2'),
    url(r'^app/$', views.app, name='app'),
    url(r'^$', views.index, name='index')
]
