# Generated by Django 4.1 on 2023-10-23 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycore', '0019_remove_contactsection_text_remove_resumesection_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='text',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
