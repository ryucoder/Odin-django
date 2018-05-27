from django.db import models
from django.core.urlresolvers import reverse


class Project(models.Model):
    name = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('project:project-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
