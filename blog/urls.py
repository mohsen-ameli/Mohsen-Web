from django.conf import settings
from django.urls import path, include

from .models import BlogPost
from .views import (post_list_view,
post_detail_view,
post_create_view,
post_update_view,
post_delete_view,

#post_create_comment,
#post_detail_comment
)


app_name = "blog"
urlpatterns = [
    path('', post_list_view, name="home"),
    path('create/', post_create_view, name="post-create"),
    path('blog/<str:slug>/', post_detail_view, name="post-detail"),
    path('blog/<str:slug>/update/', post_update_view, name="post-update"),
    path('blog/<str:slug>/delete/', post_delete_view, name="post-delete"),

    path('blog/<str:slug>/', include('comment.urls')),
    #path('blog/<str:slug>/comment', post_create_comment, name="post-comment"),
    #path('blog/<str:slug>/<int:id>', post_detail_comment, name="post-detail-comment"),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
