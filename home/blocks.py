from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from django.core.exceptions import ValidationError

class HeaderBlock(blocks.StructBlock):
    head_title = blocks.CharBlock(max_length=100, default="Jon Bergerøy", required=True)
    head_title_second = blocks.CharBlock(max_length=100, default="Fullstack Web Developer", required=True)
    head_image = ImageChooserBlock(required=False)

    class Meta:
        template = "blocks/header_block.html"  # You can create this template later
        icon = "title"  # Choose an appropriate icon from Wagtail's icon set
        label = "Header"

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

class AboutBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    text = blocks.RichTextBlock(required=True)  # Allows for multiple paragraphs and formatting

    class Meta:
        template = "blocks/about_block.html"
        icon = "image"
        label = "Image & Text"

class SocialMediaLinkBlock(blocks.StructBlock):
    name = blocks.CharBlock(
        required=True,
        help_text="Name of the social media site (e.g., GitHub, LinkedIn)."
    )
    link = blocks.URLBlock(
        required=True,
        help_text="URL to your social media profile."
    )
    logo = ImageChooserBlock(
        required=True,
        help_text="Upload the logo image for the social media site."
    )

    class Meta:
        template = "blocks/social_media_link_block.html"  # Create this template
        icon = "user"
        label = "Social Media Link"

class SocialBlock(blocks.StructBlock):
    email = blocks.CharBlock(
        required=True,
        help_text="Your email."
    )
    phone = blocks.CharBlock(
        required=True,
        help_text="Your phone number."
    )
    
    cv_document = DocumentChooserBlock(
        required=True,
        help_text="Upload your CV document."
    )

    image = ImageChooserBlock(
        required=True,
        help_text="Upload your PDF logo."
    )   

    social_media_links = blocks.ListBlock(SocialMediaLinkBlock())

    class Meta:
        template = "blocks/social_block.html"
        icon = "user"
        label = "Social Block"
