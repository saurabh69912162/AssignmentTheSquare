from django.db import models

# Create your models here.

class directors(models.Model):
    director_name = models.CharField(max_length=255,blank=False, null=False)
    age = models.IntegerField(default=0)
    director_wiki = models.URLField(max_length=2255,blank=True, null=True)

    def __str__(self):
        return self.director_name


class actors(models.Model):
    actor_name = models.CharField(max_length=255,blank=False, null=False)
    age = models.IntegerField(default=0)
    actor_wiki = models.URLField(max_length=2255,blank=True, null=True)

    def __str__(self):
        return self.actor_name


class movie_data(models.Model):
    movie_name = models.CharField(max_length=255,blank=False, null=False)
    rating = models.FloatField(default=0)
    year = models.DateField(blank=False, null=False)
    imdb_url = models.URLField(max_length=2255,blank=True, null=True)
    youtube_trailer = models.URLField(max_length=2255,blank=True, null=True)
    image = models.ImageField(upload_to='movie_thumbnails',blank=False,null=False)
    director = models.ForeignKey(directors, on_delete=models.CASCADE)
    cast1 = models.ForeignKey(actors, on_delete=models.CASCADE, related_name='actor1')
    cast2 = models.ForeignKey(actors, on_delete=models.CASCADE, related_name='actor2')


