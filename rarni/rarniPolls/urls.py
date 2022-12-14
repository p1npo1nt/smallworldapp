from django.urls import path

from . import views

#urlpatterns:
#path(route, view, name)
urlpatterns = [
    path('', views.testpage, name='rarniview'),
    path('forms/', views.rendform, name='formview')
]