from django import forms
from .models import Commenters

class CommentForm(forms.ModelForm):
	class Meta:
		model = Commenters
		fields = ['commenter_name','email','comments']