# Generated by Django 5.0 on 2023-12-25 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LatestMovies',
            fields=[
                ('m_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('genre', models.CharField(choices=[('Sci-Fi', 'Sci-Fi'), ('Thriller', 'Thriller'), ('Action', 'Action'), ('Horror', 'Horror'), ('Mystery', 'Mystery')], max_length=50)),
                ('director', models.CharField(max_length=50)),
                ('ratings', models.FloatField()),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LatestTvShows',
            fields=[
                ('m_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50)),
                ('genre', models.CharField(choices=[('Sci-Fi', 'Sci-Fi'), ('Thriller', 'Thriller'), ('Action', 'Action'), ('Horror', 'Horror'), ('Mystery', 'Mystery')], max_length=50)),
                ('ratings', models.FloatField()),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NetflixShows',
            fields=[
                ('m_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50)),
                ('genre', models.CharField(choices=[('Sci-Fi', 'Sci-Fi'), ('Thriller', 'Thriller'), ('Action', 'Action'), ('Horror', 'Horror'), ('Mystery', 'Mystery')], max_length=50)),
                ('ratings', models.FloatField()),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ThrillerShows',
            fields=[
                ('m_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50)),
                ('genre', models.CharField(choices=[('Sci-Fi', 'Sci-Fi'), ('Thriller', 'Thriller'), ('Action', 'Action'), ('Horror', 'Horror'), ('Mystery', 'Mystery')], max_length=50)),
                ('ratings', models.FloatField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]
