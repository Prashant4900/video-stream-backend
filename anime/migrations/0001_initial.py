# Generated by Django 4.0.6 on 2022-08-09 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='TagsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='SeriesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('synopsis', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('1', 'TV Show'), ('2', 'Movies'), ('3', 'Both')], max_length=1)),
                ('adult', models.BooleanField(default=False)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('banner', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='series_banner', to=settings.FILER_IMAGE_MODEL)),
                ('categories', models.ManyToManyField(blank=True, related_name='series_categories', to='anime.categoriesmodel')),
                ('poster', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='series_poster', to=settings.FILER_IMAGE_MODEL)),
                ('tags', models.ManyToManyField(blank=True, related_name='series_tags', to='anime.tagsmodel')),
            ],
            options={
                'verbose_name': 'Series',
                'verbose_name_plural': 'Series',
                'db_table': 'series',
            },
        ),
        migrations.CreateModel(
            name='SeasonsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('no', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seasons_series', to='anime.seriesmodel')),
                ('thumbnail', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='season_thumbnail', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'verbose_name': 'Season',
                'verbose_name_plural': 'Seasons',
                'db_table': 'seasons',
            },
        ),
        migrations.CreateModel(
            name='MoviesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('synopsis', models.TextField(blank=True, null=True)),
                ('adult', models.BooleanField(default=False)),
                ('source', models.URLField(blank=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('banner', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movies_banner', to=settings.FILER_IMAGE_MODEL)),
                ('categories', models.ManyToManyField(blank=True, related_name='movies_categories', to='anime.categoriesmodel')),
                ('poster', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movies_poster', to=settings.FILER_IMAGE_MODEL)),
                ('series', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movies_series', to='anime.seriesmodel')),
                ('tags', models.ManyToManyField(blank=True, related_name='movies_tags', to='anime.tagsmodel')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
                'db_table': 'movies',
            },
        ),
        migrations.CreateModel(
            name='EpisodesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True)),
                ('no', models.IntegerField(default=0)),
                ('source', models.URLField(blank=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('season', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='series', chained_model_field='series', on_delete=django.db.models.deletion.CASCADE, related_name='episodes_season', to='anime.seasonsmodel')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes_series', to='anime.seriesmodel')),
                ('thumbnail', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='episode_thumbnail', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'verbose_name': 'Episode',
                'verbose_name_plural': 'Episodes',
                'db_table': 'episodes',
            },
        ),
    ]
