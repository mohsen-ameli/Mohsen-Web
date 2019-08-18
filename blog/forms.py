from django import forms
from .models import BlogPost
from comment.models import BlogComment


class PostCreateForm(forms.ModelForm):
    title   = forms.CharField()
    content = forms.CharField(widget=forms.Textarea())
    slug = forms.SlugField()

    class Meta:
        model = BlogPost
        fields = [
            'title',
            'content',
            'image',
            'slug',
            'publish_date',
        ]


class PostCommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    title   = forms.CharField()
    content = forms.CharField(widget=forms.Textarea())
