from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, PageChooserPanel 
from wagtail.fields import StreamField
from .blocks import BootstrapCardBlock, LanguageFrameworkBlock, SocialBlock, AboutBlock, CVDownloadBlock   # Import the block here
from wagtail import blocks

class HomePage(Page):
    head_title = models.CharField(max_length=100, default="Python Fullstack Web Developer")
    head_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    about_block = StreamField([
        ('about_block', AboutBlock()),
    ], null=True, blank=True
    )
    languages_frameworks = StreamField([
        ('languages_frameworks', LanguageFrameworkBlock()),
    ], null=True, blank=True
    )
    cv = StreamField([
        ('cv_download_block', CVDownloadBlock()),
    ], null=True, blank=True
    )
    project = StreamField([
        ('card', BootstrapCardBlock()), 
    ], null=True, blank=True
    )
    social = StreamField([
        ('social', SocialBlock()), 
    ], null=True, blank=True
    )
    footer_info = StreamField([
        ('footer_info', blocks.TextBlock(template = "blocks/footer_info.html")),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("head_title"),
        FieldPanel("head_image"),
        FieldPanel('about_block'),
        FieldPanel('languages_frameworks'),
        FieldPanel('cv'),
        FieldPanel('project'),
        FieldPanel('social'),
        FieldPanel('footer_info'),
    ]
