from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import (
    ContactSection,
    PublicationsSection,
    ResumeSection,
    SiteButton,
    TextSection,
    Title,
)


def get_index_context():
    context = {}
    # Get all types of sections
    text_sections = list(TextSection.objects.all())
    resume_sections = list(ResumeSection.objects.all())
    contact_sections = list(ContactSection.objects.all())
    publications_sections = list(PublicationsSection.objects.all())
    sections = (
        text_sections + resume_sections + contact_sections + publications_sections
    )
    sections = sorted(sections, key=lambda x: x.number, reverse=False)
    context["section_list"] = sections
    # Get page title
    context["title"] = Title.objects.first()
    # Get SiteButtons
    context["sitebuttons"] = sorted(SiteButton.objects.all(), key=lambda x: x.number)
    return context


def index(request):
    context = get_index_context()
    return render(request, "mycore/index.html", context)


def test(request):
    return render(request, "mycore/test2.html", {})
