from django import forms
from .models import BlogComment


class PostCommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    title   = forms.CharField()
    content = forms.CharField(widget=forms.Textarea())
