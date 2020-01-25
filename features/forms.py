from django import forms
from .models import Feature, Comment

class FeaturePostForm(forms.ModelForm):
	class Meta:
		model = Feature
		fields = ('title', 'content')

class FeatureCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
