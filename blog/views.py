from django.shortcuts import render
from .models import Post, Commenters
from .forms import CommentForm

posts = Post.objects.all



def blog(request):
	
	return render(request, 'index.html', {'posts':posts,})
	
def single_page_blog(request, blog_id):
	posts = Post.objects.get(pk=blog_id)
	
	
	"""prev_post = Post.objects.get(pk = posts.id - 1)
	next_post = Post.objects.get(pk = posts.id + 1)"""
	related_post=Post.objects.filter(category__contains= posts.category)

	com = Commenters.objects.filter(post_id = blog_id)
	
	new_comment = None
	#comment posted
	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			# Create Comment object but don't save to database yet
			new_comment = comment_form.save(commit=False)
			# Assign the current post to the comment
			new_comment.post = posts
			# Save the comment to the database
			new_comment.save()
	else:
		comment_form = CommentForm()
		
	return render(request, 'single.html', {'posts':posts, 'related_post':related_post,'com':com,'comment_form':comment_form,})
# Create your views here.
