from django.contrib import admin

from . models import User, Post
@admin.register(Post)
class UserAdmin(admin.ModelAdmin):
	list_display = ('title', 'author','published', 'category')
	list_per_page = 10
	
@admin.register(User)
class PostAdmin(admin.ModelAdmin):
	list_display = ('name', 'username', 'email')
	list_per_page = 10

# Register your models here.
