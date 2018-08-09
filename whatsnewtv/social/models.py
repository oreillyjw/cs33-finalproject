from django.db import models
from django.contrib.auth.models import User
import json
from django.utils import timezone, formats
from .templatetags import *
from django.contrib.humanize.templatetags.humanize import date

# Create your models here.

class MovieDBInfo(models.Model):
    moviedb_id = models.CharField(max_length = 64)
    type = models.CharField(max_length = 64, blank=True)
    last_synced = models.DateTimeField(blank=True)
    created = models.DateTimeField()
    data = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if type(self.data) is dict:
            self.data = json.dumps(self.data)

        if not self.id:
            self.created = timezone.now()

        self.last_synced = timezone.now()
        super(MovieDBInfo, self).save(*args, **kwargs)

    def __str__(self):
        all_data = json.loads(self.data)
        return_info = ""
        if 'title' in all_data:
            return_info = f"{all_data['title']} ({all_data['release_date'].split('-')[0]})"
        elif 'name' in all_data:
            if 'first_air_date' in all_data and all_data['first_air_date'] is not None:
                timerange = all_data['first_air_date'].split("-")[0]
                if 'last_air_date' in all_data and not all_data['in_production']:
                    timerange = f'{timerange} - {all_data["last_air_date"].split("-")[0]}'
                else:
                    timerange += " - Present"
                return_info = f"{all_data['name']} ({timerange})"
            else:
                return_info = f"{all_data['name']}"

        return return_info

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="comment")
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length = 64, blank=True)
    moviedb = models.ForeignKey(MovieDBInfo,
            related_name="comments",
            on_delete = models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True)
    text = models.TextField(blank=True)
    approved = models.BooleanField(default=True )

    def __str__(self):
        return f"Approved: {self.approved} - {self.user} - {self.text}"


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="favorites")
    moviedb = models.ForeignKey(MovieDBInfo,
                on_delete = models.CASCADE)
    is_favorite = models.BooleanField(default=False )
    def __str__(self):
        return f"Approved: {self.is_favorite} - {self.moviedb} - {self.user}"


class Tags(models.Model):
    read = models.BooleanField( default=False )
    tagged_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="notifications")
    tagging_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="tags")
    comment = models.ForeignKey(Comment, on_delete = models.CASCADE, related_name="tagged_comment")

    def unread_count(self):
        return self.filter(read=False).count()
