from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel 
from wagtail.fields import StreamField
from .blocks import BootstrapCardBlock, LanguageFrameworkBlock, SocialBlock, AboutBlock, HeaderBlock   # Import the block here
from wagtail import blocks

class HomePage(Page):
    header_block = StreamField([
        ('header', HeaderBlock()),
    ], null=True, blank=True)
    about_block = StreamField([
        ('about_block', AboutBlock()),
    ], null=True, blank=True
    )
    languages_frameworks = StreamField([
        ('languages_frameworks', LanguageFrameworkBlock()),
    ], null=True, blank=True
    )
    project = StreamField([
        ('card', BootstrapCardBlock()), 
    ], null=True, blank=True
    )
    social = StreamField([
        ('social_block', SocialBlock())
    ], blank=True)
    footer_info = StreamField([
        ('footer_info', blocks.TextBlock(template = "blocks/footer_info.html")),
    ], null=True, blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel("header_block"),
        FieldPanel('about_block'),
        FieldPanel('languages_frameworks'),
        FieldPanel('project'),
        FieldPanel('social'),
        FieldPanel('footer_info'),
    ]
