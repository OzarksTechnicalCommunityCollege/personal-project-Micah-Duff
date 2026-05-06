from django.urls import include, path
from . import views
app_name = 'merch'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    # path('daily_feature/', views.daily_feature, name='daily_feature'),
    path('<slug:product>/',
        views.product_detail,
        name='product_detail'),
]