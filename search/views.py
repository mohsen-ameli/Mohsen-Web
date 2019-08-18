from django.shortcuts import render

from blog.models import BlogPost
from .models import SearchQuery


def search_view(request):
    query = request.GET.get('q', None)

    SearchQuery.objects.create(query=query)
    post_reaults = BlogPost.objects.search(query)
    context = {"query":query, "post_reaults": post_reaults}
    return render(request, 'search/search_query_view.html', context)
