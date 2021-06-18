from django.conf.urls import url 
from tutorials import views 
 
urlpatterns = [ 
    url(r'^api/user$', views.tutorial_list)
]