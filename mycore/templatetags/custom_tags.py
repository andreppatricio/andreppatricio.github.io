# custom_tags.py
from django import template
import markdown2

register = template.Library()

@register.filter(name='is_instance')
def is_instance(obj, class_name):
    class_name = class_name.strip()  # Remove leading/trailing whitespaces  
    return obj.__class__.__name__ == class_name

@register.filter(name='markdown_to_html')
def markdown_to_html(value):
    return markdown2.markdown(value)

@register.inclusion_tag('mycore/text_section.html')
def render_text_section(section):
    return {'section': section}


@register.inclusion_tag('mycore/resume_section.html')
def render_resume_section(section):
    return {'section': section}


@register.inclusion_tag('mycore/contact_section.html')
def render_contact_section(section):
    return {'section': section}

@register.inclusion_tag('mycore/publications_section.html')
def render_publications_section(section):
    return {'section': section}