from django.shortcuts import render,get_object_or_404,redirect
from.models import Post
from django.contrib.auth.decorators import login_required
from.forms import BlogPostForm
from django.utils import timezone

# Create your views here.
def blogposts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request,"blogposts.html", {'posts':posts})
    
def viewpost(request, id):
    post = get_object_or_404(Post, pk =id)
    # clock up the number of post views
    post.views += 1 
    post.save()
    return render(request, "viewpost.html", {'post':post})
    
@login_required
def newpost(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect(viewpost,post.pk)
    else:
        form = BlogPostForm()
    return render (request, 'blogpostform.html', {'form':form})
    
def editpost(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect(viewpost, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render (request, 'blogpostform.html', {'form':form})
    
    
# def blogposts(request, id):
#     post  = get_object_or_404(Post, pk=id)
#     post.views += 1 # clock up the number of post views
#     post.save()
#     return render(request, "viewpost.html",{'post': post})
