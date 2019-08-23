from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone

from django.contrib.contenttypes.models import ContentType

User = settings.AUTH_USER_MODEL

class BlogPostQuerySet(models.QuerySet):
    def published (self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)

    def search(self, query):
        lookup = (
                    Q(title__icontains=query) |
                    Q(content__icontains=query) |
                    Q(user__first_name__icontains=query) |
                    Q(user__last_name__icontains=query)
                 )

        return self.filter(lookup)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def search(self, query):
        if query == None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)


class BlogPost(models.Model):
    user         = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title        = models.CharField(max_length=300)
    content      = models.TextField()
    image        = models.ImageField(upload_to='images/', blank=True, null=True)
    slug         = models.SlugField(null=True, unique=True)
    publish_date = models.DateTimeField(default = timezone.now, auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp    = models.DateTimeField(auto_now_add=True)
    updated      = models.DateTimeField(default = timezone.now, auto_now=False, auto_now_add=False)

    objects      = BlogPostManager()

    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']

    def __str__(self):
        return self.title + ' - ' + str(self.id)

    @property
    def comment_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    #def get_absolute_url(self):
    #    return reverse("blog.views.post_detail_view")

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("blog:post-update", kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse("blog:post-delete", kwargs={"slug": self.slug})
