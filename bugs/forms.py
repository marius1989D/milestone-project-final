from django import forms
from .models import Bug, Comment

class BugPostForm(forms.ModelForm):
	class Meta:
		model = Bug
		fields = ('title', 'content')

class BugCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
