# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0001_initial'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=60)),
                ('body', models.TextField(blank=True)),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
                ('created_by', models.ForeignKey(related_name='blogengine_blogpost_created_by', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'permissions': (('view', 'View Blog Post'), ('edit', 'Edit Blog Post'), ('publish', 'Publish Blog Post'), ('admin', 'Alter permissions for a blog post')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='blogSlug',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('parent', models.ForeignKey(to='blogEngine.blogPost')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='mainSlug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='blogEngine.blogSlug', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='modified_by',
            field=models.ForeignKey(related_name='blogengine_blogpost_modified_by', editable=False, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='sites',
            field=models.ManyToManyField(to='sites.Site', default=[1], blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', blank=True, verbose_name='Tags', through='taggit.TaggedItem', to='taggit.Tag'),
            preserve_default=True,
        ),
    ]
