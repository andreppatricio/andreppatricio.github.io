# Generated by Django 4.1 on 2023-10-20 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycore', '0006_textsection_remove_section_text_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSection',
            fields=[
                ('section_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mycore.section')),
                ('text', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
            bases=('mycore.section',),
        ),
    ]
