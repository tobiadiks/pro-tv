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
	content = models.TextField()
	quotes = models.TextField(blank = False)
	cite = models.CharField(max_length=20, blank = False)
	tags = models.CharField(max_length = 30, help_text = "Insert tags here for better SEO ", blank = False)
	published = models.DateTimeField(default = timezone.now , editable = False)
	def __str__(self):
		return self.title
	class Meta:
		ordering = ['-published']

# Create your models here.
