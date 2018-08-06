from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.index, name='courses'),
    url(r'^courses/create$', views.create, name='create_course'),
    url(r'^courses/(?P<courseid>\d+)/delete$',views.delete, name='delete_course'),
    url(r'^courses/(?P<courseid>\d+)/destroy$',views.destroy, name='destroy_course')
]

   