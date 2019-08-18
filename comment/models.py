from django.db import models
from django.conf import settings

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from blog.models import BlogPost
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class CommentManager(models.Manager):
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(BlogPost)
        obj_id = instance.id
        queryset = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id)
        #comments = BlogComment.objects.filter(content_type=content_type, intitial=initial_data)
        return queryset


class BlogComment(models.Model):
    user            = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    #post           = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    content_type    = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id       = models.PositiveIntegerField()
    content_object  = GenericForeignKey('content_type', 'object_id')

    title           = models.CharField(max_length=100)
    content         = models.TextField()
    publish_date    = models.DateTimeField(default = timezone.now, auto_now=False, auto_now_add=False, null=True, blank=True)
    #image          = models.ImageField(upload_to='images/', blank=True, null=True)

    objects         = CommentManager()

    class Meta:
        ordering = ['-publish_date']

    def get_absolute_comment_url(self):
        return f'/blog/{self.slug}/comment'
