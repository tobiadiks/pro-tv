from django.shortcuts import render
from .models import Post, Commenters
from .forms import Comment

posts = Post.objects.all
comment_objects=Commenters.objects.all


def blog(request):
	
	return render(request, 'index.html', {'posts':posts,})
	
def single_page_blog(request, blog_id):
	posts = Post.objects.get(pk=blog_id)
	
	"""prev_post = Post.objects.get(pk = posts.id - 1)
	next_post = Post.objects.get(pk = posts.id + 1)"""
	related_post=Post.objects.filter(category__contains= posts.category)
#comment statement	
	if request.method == 'POST' :
		comment = Comment(request.POST)
		if comment.is_valid():
			commenter_name=comment.cleaned_data['cName']
			email= comment.cleaned_data['cEmail']
			comments = comment.cleaned_data['cMessage']
			
			s = Commenters(post = blog_id, commenter_name = commenter_name, email = email, comments = comments)
			
			
			s.save()
	else:
		comment = Comment()
		
	return render(request, 'single.html', {'posts':posts, 'related_post':related_post,'comment_objects':comment_objects ,})
# Create your views here.
