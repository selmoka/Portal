# Generated by Django 2.2 on 2019-04-03 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
