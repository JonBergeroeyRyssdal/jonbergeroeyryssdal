# Generated by Django 5.1 on 2024-10-04 10:00

import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_homepage_social'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='social',
            field=wagtail.fields.StreamField([('social_block', wagtail.blocks.StructBlock([('email', wagtail.blocks.CharBlock(help_text='Your email.', required=True)), ('phone', wagtail.blocks.CharBlock(help_text='Your phone number.', required=True)), ('cv_document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Upload your CV document.', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Upload your PDF logo.', required=True)), ('social_media_links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(help_text='Name of the social media site (e.g., GitHub, LinkedIn).', required=True)), ('link', wagtail.blocks.URLBlock(help_text='URL to your social media profile.', required=True)), ('logo', wagtail.images.blocks.ImageChooserBlock(help_text='Upload the logo image for the social media site.', required=True))])))]))], blank=True),
        ),
    ]
