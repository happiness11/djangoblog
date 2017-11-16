from django.shortcuts import render
from.models import Post

# Create your views here.
def blogposts(request):
    posts = Post.objects.all()
    return render(request,"blogposts.html", {'posts':posts})