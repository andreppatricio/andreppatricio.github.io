from django.contrib import admin

from .models import TextSection, ResumeSection, ResumeEntry, ContactSection, PublicationsSection, Publication, Title, SiteButton


class TextSectionAdmin(admin.ModelAdmin):
    list_display = ('number', 'short_title', 'title', 'text')

class ResumeEntryInline(admin.StackedInline):
    model = ResumeEntry

class ResumeSectionAdmin(admin.ModelAdmin):
    list_display = ('number', 'short_title', 'title', 'text')
    inlines = [ResumeEntryInline]

class ContactSectionAdmin(admin.ModelAdmin):
    list_display = ('number', 'short_title', 'title', 'text', 'email')

class PublicationInline(admin.StackedInline):
    model = Publication

class PublicationSectionAdmin(admin.ModelAdmin):
    list_display = ('number', 'short_title', 'title', 'text')
    inlines = [PublicationInline]

class TitleAdmin(admin.ModelAdmin):
    list_display = ('main_text', 'secondary_text')

class SiteButtonAdmin(admin.ModelAdmin):
    list_display = ('number', 'text', 'url', 'icon')


admin.site.register(TextSection, TextSectionAdmin)
admin.site.register(ResumeSection, ResumeSectionAdmin)
admin.site.register(ContactSection, ContactSectionAdmin)
admin.site.register(PublicationsSection, PublicationSectionAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(SiteButton, SiteButtonAdmin)

from .models import SiteSettings

def toggle_push_static(modeladmin, request, queryset):
    # Assuming a single instance of SiteSettings
    settings = SiteSettings.objects.first()
    if settings:
        settings.push_static = not settings.push_static
        settings.save()

toggle_push_static.short_description = "Toggle Push of Static Files on DB alteration"

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['push_static']
    actions = [toggle_push_static]