# Generated by Django 4.1 on 2023-10-24 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycore', '0020_alter_section_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_flag_enabled', models.BooleanField(default=False)),
            ],
        ),
    ]
