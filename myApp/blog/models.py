from django.db import models
from django import forms
class Post(models.Model):
	text = models.TextField(max_length=250)
	time = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.text

class PostForm(forms.Form):
	text = forms.CharField(
		max_length=250, widget=forms.Textarea)

	