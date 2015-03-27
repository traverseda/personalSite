from django.contrib import admin
from blogEngine.models import blogPost, blogSlug
# Register your models here.

class abstractMetaData(admin.ModelAdmin):
    readonly_fields = ('modified', 'created','modified_by', 'created_by')
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.modified_by = request.user
            if not obj.created_by:
               obj.created_by = request.user
        super(abstractMetaData, self).save_model(request, obj, form, change)

class slugInline(admin.TabularInline):
    model = blogSlug


class blogPostAdmin(abstractMetaData):
    inlines = [slugInline]
    pass
#    search_fields = ["title"]
admin.site.register(blogPost, blogPostAdmin)


