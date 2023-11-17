# Generated by Django 4.1 on 2023-10-20 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycore', '0005_rename_reduced_title_section_short_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextSection',
            fields=[
                ('section_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mycore.section')),
                ('text', models.CharField(max_length=200)),
            ],
            bases=('mycore.section',),
        ),
        migrations.RemoveField(
            model_name='section',
            name='text_content',
        ),
        migrations.AddField(
            model_name='resumesection',
            name='text',
            field=models.CharField(default='None', max_length=200),
            preserve_default=False,
        ),
    ]
