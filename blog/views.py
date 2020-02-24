from django.shortcuts import render
from .models import Post
posts = Post.objects.all

def blog(request):
	
	return render(request, 'index.html', {'posts':posts,})
	
def single_page_blog(request, blog_id):
	posts = Post.objects.get(pk=blog_id)
	
	"""prev_post = Post.objects.get(pk = posts.id - 1)
	next_post = Post.objects.get(pk = posts.id + 1)"""
	related_post=Post.objects.all().filter(category__contains= posts.category)
	return render(request, 'single.html', {'posts':posts, 'related_post':related_post,})
# Create your views here.
