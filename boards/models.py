from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Sport(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(default='')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     kwargs = {
    #         'slug': self.slug,
    #         #'pk': self.pk
    #     }
    #     return reverse('sport_skills', kwargs=kwargs)

class Skill(models.Model):
    name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, related_name='skills')
    link = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)
    player_name = models.CharField(max_length=100)
    tags = models.CharField(max_length=300, null=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
