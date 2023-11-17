from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry
from django.template import loader

from .models import SiteSettings
from .views import get_index_context

import push_static_files

@receiver(post_save, sender=LogEntry)
def model_change_handler(sender, instance, **kwargs):

    print(f"Change detected in model {sender._meta.object_name} with ID {instance.id} - {instance}")
    # # Get settings to check if it should push static files to Git
    settings = SiteSettings.objects.first()
    if settings.push_static and not SiteSettings.__name__ in instance.object_repr:
        print("\nPush static files\n")
        template = loader.get_template('mycore/index.html')
        context = get_index_context()
        rendered_template = template.render(context)
        push_static_files.main(rendered_template, instance)
    else:
        print("\nNo push\n")

