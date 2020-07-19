from django.urls import path 
from . import views
from .views import HomeView

app_name = 'core'

urlpatterns = [
    #path('', views.home, name="home" ) 
    path('', HomeView.as_view(), name = "home"),

]