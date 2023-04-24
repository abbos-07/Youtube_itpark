# Generated by Django 3.2.18 on 2023-04-19 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1500)),
                ('poster', models.ImageField(upload_to='poster/')),
                ('video', models.FileField(upload_to='video_file/')),
                ('channel', models.CharField(max_length=255)),
            ],
        ),
    ]
