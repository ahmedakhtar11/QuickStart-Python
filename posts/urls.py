# Posts App URLs ==>

from django.conf.urls import url


from django.contrib import admin
from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [

    # Admin Page ==>
    path('admin/', admin.site.urls),

    # Test Pages ==>
    url(r'^test1/$', views.test1, name='test1'),
    url(r'^test2/$', views.test2, name='test2'),
   
    # Direct /app URL to App ==>
    url(r'^app/$', views.app, name='app'),

    # Direct No URL to App ==>
    url(r'^$', views.app, name='app'),
    url(r'^details/(?P<id>\d+)/$', views.details, name='details')
]
