# Generated by Django 4.1 on 2023-10-23 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycore', '0017_alter_resumesection_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumesection',
            name='text',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
