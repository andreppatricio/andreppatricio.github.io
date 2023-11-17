# Generated by Django 4.1 on 2023-10-20 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycore', '0007_contactsection'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationsSection',
            fields=[
                ('section_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mycore.section')),
            ],
            bases=('mycore.section',),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=100)),
                ('doi', models.CharField(max_length=50)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycore.publicationssection')),
            ],
        ),
    ]
