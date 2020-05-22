
from django.urls import path, re_path
from . import views


urlpatterns = [
  
    re_path('^$',views.index, name = 'home'),
    path('',views.landing, name = 'landing'),
    path('aboretum', views.aboretum_images, name = "aboretum"),
    path('nature', views.nature_images, name = "nature"),
    path('park', views.park_images, name = "park"),
    path('beach', views.beach_images, name = "beach"),
    path('cgi', views.cgi_images, name = "cgi"),
    re_path('^search/',views.search_results, name = 'search_results'),
]