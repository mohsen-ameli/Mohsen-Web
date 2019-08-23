from django.db import models


class SearchQuery(models.Model):
    query = models.CharField(max_length=300)
