from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf.urls import include, url

urlpatterns = [
    #path('', views.index, name='index'),
    path('map/<input_time>/',views.map, name='map'),
    path('map/',views.map, name='map'),
    path('luasmap/',views.map_luas, name='map_luas'),
    path('dartmap/',views.map_dart, name='map_dart'),
    path('', views.homepage, name='homepage'),
    path('luas/', views.luas, name='luas'),
    #path('bike/<timeIn>', views.bike, name='bike'),
    path('dart/', views.dart, name='dart'),
    path('analytics/', views.analytics, name='analytics'),
    path('form/', views.form, name='form'),
    path('test/', views.test, name = 'test'),
    #url(r'^form/', TemplateView.as_view(template_name="form.html"),
    #               name='form'),
]
