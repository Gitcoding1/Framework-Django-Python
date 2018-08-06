from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^users$', views.index, name="users"),
  url(r'^users/create$', views.create, name= 'create_user'),
  url(r'^users/new$', views.new_user, name='new_user'),
  url(r'^user/(?P<userid>\d+)$', views.show, name='show_user'),
  url(r'^users/edit/(?P<userid>\d+)$', views.edit, name='edit_user'),
  url(r'^users/(?P<userid>\d+)/update$', views.update, name = 'update_user'),
  url(r'^users/(?P<userid>\d+)/delete$', views.delete, name='delete_user'),
]