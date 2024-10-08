# Generated by Django 5.1 on 2024-10-04 11:24

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_homepage_about_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='about_block',
            field=wagtail.fields.StreamField([('about_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('text', wagtail.blocks.RichTextBlock(required=True))]))], blank=True, null=True),
        ),
    ]
