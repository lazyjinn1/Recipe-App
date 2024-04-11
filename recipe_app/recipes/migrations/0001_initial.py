# Generated by Django 4.2.11 on 2024-04-10 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=50)),
                ('ingredients', models.CharField(max_length=200)),
                ('cooking_time', models.FloatField(help_text='in minutes')),
                ('difficulty', models.CharField(max_length=20)),
                ('note', models.TextField()),
            ],
        ),
    ]
