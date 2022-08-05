from django.shortcuts import render

from posts.models import Post

# Create your views here.
def all_posts(request):
    posts = Post.objects.all()
    return render(request,'posts.html',{'mahmoud':posts})
    

def single_post(request,id):
    post = Post.objects.get(id=id)
    return render(request,'single.html',{'single_post':post})