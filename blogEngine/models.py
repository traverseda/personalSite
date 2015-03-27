from django.db import models
import reversion
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.cache import cache
import markdown2


def markdownify(text, strip=True):
    extensions = [
        "footnotes",
        "code-friendly",
        "fenced-code-blocks",
        "smarty-pants",
        "tables",
        "cuddled-lists"
    ]
    if strip==True:
        return markdown2.markdown(text,extras=extensions, safe_mode="escape")
    if strip==False:
        return markdown2.markdown(text,extras=extensions, safe_mode=False)

class abstractMetaData(models.Model):
    modified=models.DateTimeField(auto_now=True, editable=False)
    created=models.DateTimeField(auto_now_add=True, editable=False)
    modified_by=models.ForeignKey(User, editable=False,related_name="%(app_label)s_%(class)s_modified_by", null=True)
    created_by=models.ForeignKey(User,editable=False,related_name="%(app_label)s_%(class)s_created_by", null=True)
    sites = models.ManyToManyField(Site, blank=True, default=[1])
    class Meta:
        abstract = True

class blogPost(abstractMetaData):
    title = models.CharField(max_length=60,blank=True)
    authors = models.ManyToManyField(User, blank=True)
    publishDate=models.DateTimeField(blank=True, null=True)
    body = models.TextField(blank=True)
    tags = TaggableManager(blank=True)
    ##Optionally, set one of the slugs as primary. Tjis should get automatically appended onto the url.
    mainSlug = models.ForeignKey('blogSlug', on_delete=models.SET_NULL, null=True, blank=True)

    ##This here renders the body. It also does it's best to cache it.
    ##We need to be careful to unset it whenever it's modified. So basically on any save.
    def renderedBody(self):
        return(markdownify(self.body))
        renderedBody = cache.get("blogPost {pk} rendered body".format(pk=self.pk), None)
        if not renderedBody:
            cache.set("blogPost {pk} rendered body".format(pk=self.pk), 'Initial value')


    class Meta:
        permissions = (
            ('view', 'View Blog Post'),
            ('edit', 'Edit Blog Post'),
            ('publish', 'Publish Blog Post'),
            ('admin', 'Alter permissions for a blog post'),
        )

    def __str__(self):
        if self.mainSlug:
            return str(self.mainSlug)
        else:
            return str(self.title)

#reversion.register(blogPost, follow=['blogSlug'])

class blogSlug(models.Model):
    ##Why do this in a different table? Cool url's *never* change, and that means creating a new slug if you mis-type. Also means you can have multiple urls direct to one post.
    parent = models.ForeignKey(blogPost)
    slug=models.SlugField(unique=True,)
    def __str__(self):
        return self.slug

