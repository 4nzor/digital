# Generated by Django 2.0.2 on 2018-03-14 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='org',
            name='full_name',
            field=models.CharField(default='org', max_length=200),
            preserve_default=False,
        ),
    ]
