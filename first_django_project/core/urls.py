from django.urls import path 
from . import views
from .views import HomeView, ArticleView

app_name = 'core'

urlpatterns = [
    #path('', views.home, name="home" ) 
    path('', HomeView.as_view(), name = "home"),
    path('article/<int:pk>', ArticleView.as_view(), name='article-detail'),
    path('base',views.base, name="base"),
]