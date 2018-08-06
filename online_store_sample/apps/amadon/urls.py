from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.index),
  url(r'^purchased/(?P<item_id>\d+)',views.process_order),
  url(r'^checkout', views.checkout)
]