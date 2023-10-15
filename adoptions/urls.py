from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adopt/filter/', views.filter, name='filter'),
    path('adopt/', views.adopt, name='adopt'),
    path('rehomeform/rehome/', views.rehome, name='rehome'),
    path('rehomeform/rehome/rehomerform/rehomer/', views.rehomer, name='rehomer'),
    path('rehomeform/', views.rehomeform, name='rehomeform'),
    path('rehomeform/rehome/rehomerform/', views.rehomerform, name='rehomerform'),
    path('rehomeform/rehome/rehomerform/rehomer/backhome/', views.backhome, name='backhome'),
    path('adopt/filter/', views.filter, name='filter'),
    path('adopt/backadopt/', views.backadopt, name='backadopt'),
    path('adopt/filter/backadopt/', views.backadopt, name='backadopt'),
    path('adopt/rehomerform/',views.rehomerform, name='adoption'),
    path('adopt/rehomerform/rehomer/', views.rehomer, name='adoptionrehomer'),
    path('adopt/rehomerform/rehomer/backhome', views.backhome, name='adoptionbackhome'),
]
