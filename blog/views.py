from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.contrib.contenttypes.models import ContentType

from .models import BlogPost
from comment.models import BlogComment
from .forms import PostCreateForm, PostCommentForm

from django.urls import reverse

"CRUD : Create Retrieve Update Delete"



def post_list_view(request):
    qs = BlogPost.objects.all()#.published()
    template_name = "blog/post_list_view.html"
    context = {"object_list": qs}
    return render(request, template_name, context)


@login_required
def post_create_view(request):
    form = PostCreateForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = PostCreateForm()
    template_name = "blog/post_create.html"
    context = {"form": PostCreateForm}
    return render(request, template_name, context)


def post_detail_view(request, slug):
    instance = get_object_or_404(BlogPost, slug=slug)

    initial_data = {
        "content_type": instance.comment_content_type,
        "object_id": instance.id
    }
    form_ = PostCommentForm(request.POST or None, initial=initial_data)

    if form_.is_valid():
        print(form_.cleaned_data)
        #form_.save()
        #form_ = PostCommentForm()

        #c_type = form_.cleaned_data.get("content_type")
        #content_type = ContentType.objects.get(model=c_type)
        content_type = ContentType.objects.get_for_model(BlogPost)
        object_id = form_.cleaned_data.get("object_id")
        title = form_.cleaned_data.get("title")
        content_info = form_.cleaned_data.get("content")

        new_comment, created = BlogComment.objects.get_or_create(
            user = request.user,
            content_type = content_type,
            object_id = object_id,
            title = title,
            content = content_info
        )
        #return HttpResponseRedirect(redirect_to="blog:post-update")
        #return reverse("blog:post-detail", kwargs={"slug": self.slug})
        if created:
            print("yea it worked !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    comments = BlogComment.objects.filter_by_instance(instance)

    context = {"post": instance, "form": form_, "comments":comments}
    template_name = "blog/post_detail_view.html"
    return render(request, template_name, context)


@login_required
def post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = PostCreateForm(request.POST or None, request.FILES or None ,instance=obj)

    if form.is_valid():
        form.save()

    template_name = "blog/post_update.html"
    context = {"form": form}
    return render(request, template_name, context)


@login_required
def post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)

    if request.method == "POST":
        obj.delete()
        return redirect('/')

    template_name = "blog/post_delete_view.html"
    context = {"object_list": obj}
    return render(request, template_name, context)





'''
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
class PostView(ListView):
    template_name = "blog/post_view.html"
    queryset = BlogPost.objects.all()


class PostDetailView(DetailView):
    template_name = "blog/post_detail_view.html"
    context_object_name = 'post'
    queryset = BlogPost.objects.all()


class PostCreateView(CreateView):
    template_name = "blog/post_create.html"
    form_class = PostCreateForm
    queryset = BlogPost.objects.all()
'''
