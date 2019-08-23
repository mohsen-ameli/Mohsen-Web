from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import BlogComment
from blog.models import BlogPost
from .forms import PostCommentForm

from django.contrib.contenttypes.models import ContentType

'''
@login_required
def post_create_comment(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)

    context = {"form": form_}
    template_name = 'blog/post_comment.html'
    return render(request, template_name, context)


@login_required
def post_detail_comment(request, id):
    obj_ = BlogComment.objects.all()
    template_name = "blog/comment_detail_view.html"
    context = {"post_": obj_}
    return render(request, template_name, context)
'''
