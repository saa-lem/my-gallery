
from django.urls import path, re_path
from . import views
from django.conf.urls import url

urlpatterns = [
  
    re_path('images/',views.index, name = 'home'),
    path('',views.landing, name = 'landing'),
    path('Places', views.places_images, name = "Places"),
    path('Nature', views.nature_images, name = "Nature"),
    path('Animals', views.park_images, name = "Animals"),
    path('Beach', views.beach_images, name = "Beach"),
    re_path('^search/',views.search_results, name = 'search_results'),
]