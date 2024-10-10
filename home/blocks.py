from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
<<<<<<< HEAD

class HeaderBlock(blocks.StructBlock):
    head_title = blocks.CharBlock(max_length=100, default="Jon Bergerøy", required=True)
    head_title_second = blocks.CharBlock(max_length=100, default="Fullstack Web Developer", required=True)
    head_image = ImageChooserBlock(required=False)

    class Meta:
        template = "blocks/header_block.html"  # You can create this template later
        icon = "title"  # Choose an appropriate icon from Wagtail's icon set
        label = "Header"
=======
import uuid
>>>>>>> 2a2270661ecdc3596b76af2f729e56622e350256

from django.core.exceptions import ValidationError

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

<<<<<<< HEAD
class AboutBlock(blocks.StructBlock):
=======
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock

class CVDownloadBlock(blocks.StructBlock):
    CHOICES = [
        ('file', 'File'),
        ('link', 'Link'),
    ]
    
    pdf_logo = ImageChooserBlock(required=True, help_text="Logo to represent the PDF download")
    option = blocks.ChoiceBlock(choices=CHOICES, required=True, help_text="Choose between uploading a file or using a link")
    cv_file = DocumentChooserBlock(required=False, help_text="Upload the CV document (if 'File' is selected)")
    external_link = blocks.URLBlock(required=False, help_text="External URL for CV (if 'Link' is selected)")

    class Meta:
        template = "blocks/cv_download_block.html"
        icon = "doc-full-inverse"
        label = "CV Download Block"

    def clean(self, value):
        """
        Validation: Ensure that either `cv_file` or `external_link` is provided based on the chosen option.
        """
        cleaned_data = super().clean(value)
        if cleaned_data['option'] == 'file' and not cleaned_data.get('cv_file'):
            raise blocks.ValidationError('You must upload a file when "File" option is selected.')
        elif cleaned_data['option'] == 'link' and not cleaned_data.get('external_link'):
            raise blocks.ValidationError('You must provide a link when "Link" option is selected.')
        return cleaned_data


class AboutBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    text = blocks.TextBlock(required=True)

    class Meta:
        template = "blocks/about_block.html"
        icon = "image"
        label = "Image & Text"

class LanguageFrameworkBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=100)
>>>>>>> 2a2270661ecdc3596b76af2f729e56622e350256
    image = ImageChooserBlock(required=True)
    text = blocks.RichTextBlock(required=True)  # Allows for multiple paragraphs and formatting

    class Meta:
        template = "blocks/about_block.html"
        icon = "image"
        label = "Image & Text"

class LanguageFrameworkBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    description = blocks.RichTextBlock(required=True)

    class Meta:
        template = "blocks/languages_frameworks.html"
        icon = "doc-full"
        label = "Language Framework"


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
<<<<<<< HEAD
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
=======
    CHOICES = [
        ('url', 'URL'),
        ('email', 'Email'),
    ]
    
    logo = ImageChooserBlock(required=True)
    option = blocks.ChoiceBlock(choices=CHOICES, required=True, help_text="Choose whether this is a URL or an email.")
    url = blocks.URLBlock(required=False, help_text="URL of the social profile (if 'URL' is selected).")
    email = blocks.EmailBlock(required=False, help_text="Email address (if 'Email' is selected).")

    class Meta:
        template = "blocks/social.html"
        icon = "doc-full"
        label = "Social Media Logo and Link"

    def clean(self, value):
        """
        Validation: Ensure that either `url` or `email` is provided based on the chosen option.
        """
        cleaned_data = super().clean(value)
        if cleaned_data['option'] == 'url' and not cleaned_data.get('url'):
            raise ValidationError('You must provide a URL when "URL" option is selected.')
        elif cleaned_data['option'] == 'email' and not cleaned_data.get('email'):
            raise ValidationError('You must provide an email address when "Email" option is selected.')
        return cleaned_data

class AboutBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    text = blocks.TextBlock(required=True)

    class Meta:
        template = "blocks/about_block.html"
        icon = "image"
        label = "Image & Text"
>>>>>>> 2a2270661ecdc3596b76af2f729e56622e350256
