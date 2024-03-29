# Generated by Django 4.2.9 on 2024-01-25 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('content', models.TextField(max_length=2000)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('excerpt', models.TextField(blank=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('meal_type', models.CharField(choices=[('chicken', 'Chicken'), ('fish', 'Fish'), ('meat', 'Meat'), ('vegitarian', 'Vegitarian'), ('vegan', 'Vegan')], default='fish', max_length=50)),
                ('effort', models.CharField(choices=[('bad_day_comfort_food', 'Bad day comfort food'), ('trying_a_healthy_day', 'Trying a healthy day'), ('im_in_a_hurry', "I'm in a hurry"), ('i_have_time_but_no_brains', 'I have time but no brains')], default='Bad day comfort food', max_length=50)),
                ('image_alt', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
