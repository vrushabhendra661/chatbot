# Generated by Django 3.2.9 on 2021-11-14 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stupidcount', models.IntegerField(default=0)),
                ('fatcount', models.IntegerField(default=0)),
                ('dumbcount', models.IntegerField(default=0)),
            ],
        ),
    ]
