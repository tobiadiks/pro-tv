from django.db import models
from django.utils import timezone

class User(models.Model):
	name = models.CharField(max_length = 150)
	email = models.EmailField()
	username = models.CharField(max_length = 100, unique=True)
	def __str__(self):
		return self.name
		
class Post(models.Model):
	categories = [
	('Tech', 'Tech'),
	('Fashion', 'Fashion'),
	('Education', 'Education'),
	('Lifestyle', 'Lifestyle'),
	('Unknown', 'Unknown'),
	]
	
	title = models.CharField(max_length = 60)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	category = models.CharField(max_length = 100)
image = models.URLField(help_text ='your image imgbb link')
	content = models.TextField()
	quotes = models.TextField(blank = True , help_text = "Not Compulsory")
	cite = models.CharField(max_length=20, blank = True , help_text = "leave it empty if quotes are empty")
	tags = models.CharField(max_length = 30, help_text = "Insert tags here for better SEO ", blank = False , default = "Protv")
	published = models.DateTimeField(default = timezone.now , editable = False)

	def __str__(self):
		return self.title
	class Meta:
		ordering = ['-published']
		
class Commenters(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	commenter_name = models.CharField(max_length = 50)
	email = models.EmailField(blank = True)
	comments = models.TextField()
	comment_time = models.DateTimeField(default = timezone.now, editable = False)
	def __str__(self):
		return self.email
	class Meta:
		ordering = ['comment_time']
	
	
# Create your models here.
