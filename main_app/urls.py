from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.show, name='show'),
    url(r'^post_url/$', views.post_treasure, name='post_treasure'),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^like_treasure/$', views.like_treasure, name='like_treasure'),
    url(r'^api_call/$', views.api_call, name='api_call'),
]
