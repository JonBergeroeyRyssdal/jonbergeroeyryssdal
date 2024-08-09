from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, PageChooserPanel 
from wagtail.fields import StreamField
from .blocks import BootstrapCardBlock, LanguageFrameworkBlock, SocialBlock  # Import the block here
from wagtail import blocks

class HomePage(Page):
    head_title = models.CharField(max_length=100, default="Python Fullstack Web Developer")
    head_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    about_text = StreamField([
        ('paragraph', blocks.RichTextBlock()),
    ], null=True)
    about_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    languages_frameworks = StreamField([
        ('languages_frameworks', LanguageFrameworkBlock()),
    ], null=True, blank=True)
    PDF_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    CV = models.FileField(upload_to='documents/', blank=True, null=True
                          )
    project = StreamField([
        ('card', BootstrapCardBlock()), 
    ], null=True
    )
    social = StreamField([
        ('social', SocialBlock()), 
    ], null=True
    )
    footer_info = StreamField([
        ('footer_info', blocks.TextBlock(template = "blocks/footer_info.html")),
    ], null=True)

    content_panels = Page.content_panels + [
        FieldPanel("head_title"),
        PageChooserPanel("head_image"),
        PageChooserPanel("about_image"),
        FieldPanel("about_text"),
        FieldPanel('languages_frameworks'),
        PageChooserPanel("PDF_logo"),
        FieldPanel('CV'),
        FieldPanel('project'),
        FieldPanel('social'),
        FieldPanel('footer_info'),
    ]
