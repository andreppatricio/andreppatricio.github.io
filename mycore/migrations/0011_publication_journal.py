# Generated by Django 4.1 on 2023-10-21 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycore', '0010_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='journal',
            field=models.CharField(default='None', max_length=100),
            preserve_default=False,
        ),
    ]
