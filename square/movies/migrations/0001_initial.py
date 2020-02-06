# Generated by Django 3.0.2 on 2020-02-05 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='actors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_name', models.CharField(max_length=255)),
                ('age', models.IntegerField(default=0)),
                ('actor_wiki', models.URLField(blank=True, max_length=2255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='directors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_name', models.CharField(max_length=255)),
                ('age', models.IntegerField(default=0)),
                ('director_wiki', models.URLField(blank=True, max_length=2255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='movie_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=255)),
                ('rating', models.FloatField(default=0)),
                ('year', models.DateField()),
                ('imdb_url', models.URLField(blank=True, max_length=2255, null=True)),
                ('youtube_trailer', models.URLField(blank=True, max_length=2255, null=True)),
                ('image', models.ImageField(upload_to='movie_thumbnails')),
                ('cast1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actor1', to='movies.actors')),
                ('cast2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actor2', to='movies.actors')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.directors')),
            ],
        ),
    ]
