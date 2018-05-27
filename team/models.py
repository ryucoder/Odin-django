from django.db import models
from django.core.urlresolvers import reverse


class Team(models.Model):
    designation_choices = (
        ('pm', 'Project Manager'),
        ('po', 'Product Owner'),
        ('ba', 'Business Analyst'),
        ('sm', 'Scrum Master'),
        ('fe', 'Front End Developer'),
        ('be', 'Back End Developer'),
        ('fs', 'Full Stack Developer'),
        ('mt', 'Manual Tester'),
        ('at', 'Automation Tester'),
    )

    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    designation = models.CharField(max_length=256, choices=designation_choices, default="pm")
    joining_date = models.DateTimeField(null=True, blank=True)
    relieving_date = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('team:team-detail', kwargs={'pk': self.pk})

    @property
    def full_name(self):
        return self.first_name + self.last_name
    
    def __str__(self):
        return self.full_name
