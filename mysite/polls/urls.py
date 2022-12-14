from django.urls import path

from . import views

#urlpatterns:
#path(route, view, name)
urlpatterns = [
    path('rarni/', views.testpage, name='rarniview'),
    path("rarni/<int:id>", views.index, name="index"),
    path("rarni/create/", views.create, name="index"),
    path("rarni/<int:id>", views.index, name="index"),
    # path('sizenew/', include())
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    path('sizenew/', views.sizepage, name='sizepage'),
    path('sizenew/<int:size_id>/', views.sizepage_detail, name="spdetail"),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]