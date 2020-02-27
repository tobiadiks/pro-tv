from django.contrib import admin

from . models import User, Post, Commenters
admin.site.site_headers = "ProTv Dashboard('Please do not tamper with any other link, only use the Post and User link under the Blog' "
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author','published', 'category')
	list_per_page = 10
	
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('name', 'username', 'email')
	list_per_page = 10
	
@admin.register(Commenters)
class CommentersAdmin(admin.ModelAdmin):
	list_display = ( 'commenter_name', 'comments')
	list_per_page = 20


# Register your models here.
