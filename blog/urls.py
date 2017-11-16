from django.conf.urls import url
from.views import blogposts




urlpatterns = [
    url(r'^post', blogposts, name="post"),
    
    ]