from django.db import models


class Section(models.Model):
    number = models.PositiveSmallIntegerField()
    short_title = models.CharField(max_length=15, default="None")
    title = models.CharField(max_length=20)
    text = models.TextField(max_length=1000, blank=True)

    def numbered_title(self):
        return f"0{self.number}. {self.title}"

    def numbered_short_title(self):
        return f"0{self.number}. {self.short_title}"

    def __str__(self):
        return self.title


class TextSection(Section):
    """Text Section with just text (inhereted from Section)"""


class ResumeSection(Section):
    """Resume Section with text (inhereted from Section) and ResumeEntries"""


class ResumeEntry(models.Model):
    section = models.ForeignKey(ResumeSection, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    workplace = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, default=None)
    description = models.TextField(max_length=1000, blank=True)
    link = models.CharField(max_length=200)


class ProjectSection(Section):
    """Resume Section with text (inhereted from Section) and ResumeEntries"""


class ProjectEntry(models.Model):
    section = models.ForeignKey(ProjectSection, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)
    link = models.CharField(max_length=200)


class ContactSection(Section):
    email = models.EmailField()


class PublicationsSection(Section):
    """Publications"""


class Publication(models.Model):
    section = models.ForeignKey(PublicationsSection, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=100)
    journal = models.CharField(max_length=100)
    doi = models.CharField(max_length=50)


class Title(models.Model):
    main_text = models.CharField(max_length=50)
    secondary_text = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # To ensure only one instance exists, delete all existing instances before saving
        self.__class__.objects.exclude(pk=self.pk).delete()
        super(Title, self).save(*args, **kwargs)


class SiteButton(models.Model):
    number = models.PositiveSmallIntegerField()
    text = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    icon = models.FileField(upload_to="sitebuttons")

    def __str__(self):
        return self.text


class SiteSettings(models.Model):
    push_static = models.BooleanField(default=False)

    @classmethod
    def get_sitewide_settings(cls):
        # Get the single instance or create it if it doesn't exist
        settings, created = cls.objects.get_or_create(pk=1)
        return settings

    def save(self, *args, **kwargs):
        # To ensure only one instance exists, delete all existing instances before saving
        self.__class__.objects.exclude(pk=self.pk).delete()
        super(SiteSettings, self).save(*args, **kwargs)
