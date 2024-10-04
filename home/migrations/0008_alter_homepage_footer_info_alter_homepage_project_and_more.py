# Generated by Django 5.1 on 2024-08-18 19:21

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_homepage_pdf_logo_alter_homepage_head_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='footer_info',
            field=wagtail.fields.StreamField([('footer_info', wagtail.blocks.TextBlock(template='blocks/footer_info.html'))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='project',
            field=wagtail.fields.StreamField([('card', wagtail.blocks.StructBlock([('id', wagtail.blocks.CharBlock(help_text='Unique identifier for the card', required=True)), ('title', wagtail.blocks.CharBlock(help_text='Add your card title', required=True)), ('text', wagtail.blocks.TextBlock(help_text='Add your card text', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Add an image', required=True)), ('live_url', wagtail.blocks.TextBlock(help_text='Add URL for live demo (optional)', required=False)), ('git_url', wagtail.blocks.TextBlock(help_text='Add URL for GitHub repository', required=True))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='social',
            field=wagtail.fields.StreamField([('social', wagtail.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=True)), ('url', wagtail.blocks.URLBlock(required=True))]))], blank=True, null=True),
        ),
    ]
