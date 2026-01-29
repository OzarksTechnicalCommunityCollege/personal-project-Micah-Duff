from django.urls import path
from . import views
app_name = 'comic'
urlpatterns = [
    #post views
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail,
        name='post_detail'),
    path('<int:post_id>/share/', views.comic_share, name='comic_share'),
]