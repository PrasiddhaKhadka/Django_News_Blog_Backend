from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.news_list),
    path('list/<int:pk>', views.news_detail,name='news_detail'),
]