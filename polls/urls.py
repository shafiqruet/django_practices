from django.urls import path
from django.contrib import admin


from . import views
from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='details'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id/votes/', views.vote, name='votes'),

]
