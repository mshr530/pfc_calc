# Generated by Django 3.1.7 on 2021-06-25 00:10

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('blog', '0012_blog_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='複数加える場合は, で区切ってください', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
