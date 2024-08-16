from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
import uuid

class BootstrapCardBlock(blocks.StructBlock):
    id = blocks.CharBlock(
        required=True,
        help_text="Unique identifier for the card"
    )
    title = blocks.CharBlock(
        required=True,
        help_text="Add your card title"
    )
    text = blocks.TextBlock(
        required=True,
        help_text="Add your card text"
    )
    image = ImageChooserBlock(
        required=True,
        help_text="Add an image"
    )
    live_url = blocks.TextBlock(
        required=False,
        help_text="Add URL for live demo (optional)"
    )
    git_url = blocks.TextBlock(
        required=True,
        help_text="Add URL for GitHub repository"
    )

    class Meta:
        template = "blocks/bootstrap_card.html"
        icon = "doc-full"
        label = "Bootstrap Card"

class LanguageFrameworkBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=100)
    image = ImageChooserBlock(required=True)
    description = blocks.TextBlock(required=True)
    

    class Meta:
        template = "blocks/languages_frameworks.html"
        icon = "doc-full"
        label = "Language Framework"

class SocialBlock(blocks.StructBlock):
    logo = ImageChooserBlock(required=True)
    url = blocks.URLBlock(required=True)  # Changed to URLBlock to ensure proper URL validation
    
    class Meta:
        template = "blocks/social.html"
        icon = "doc-full"
        label = "Social media logo and link to profile"

class AboutBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    text = blocks.RichTextBlock(required=True)

    class Meta:
        template = "blocks/AboutBlock.html"
        icon = "image"
        label = "Image & Text"