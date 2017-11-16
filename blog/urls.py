from django.conf.urls import url
from .views import blogposts,viewpost,newpost,editpost





urlpatterns = [
    url(r'^post$', blogposts, name="posts"),
    url(r'^post/(\d+)$', viewpost,name="viewpost"),
    url(r'^post/add', newpost, name="newpost"),
    url(r'^post/(\d+)/edit$', editpost, name="editpost")
    ]