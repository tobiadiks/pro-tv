from django import forms
from django.core import validators
from django.utils import timezone

def comment_size(value):
	if len(value) < 1 :
		raise forms.ValidationError("Your Comment is Empty")
		
class Comment(forms.Form):
	name = forms.CharField(required = True , help_text ="First Name")
	email = forms.EmailField(required = False )
	comment = forms.CharField(required = True, validators = [comment_size, ])
	