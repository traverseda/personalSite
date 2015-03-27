from django.shortcuts import render, redirect, get_object_or_404
from blogEngine.models import blogPost, blogSlug

def postList(request, pk):
    pass

##Both of these just deal with url management, and keeping url's human readable.
def postView(request, pk=None, slug=None):
    postInstance = get_object_or_404(blogPost, pk=pk)
    #redirects you to the proper name, if you're not using it.
    if postInstance.mainSlug and (not slug or postInstance.mainSlug.slug != slug):
        return redirect(postView, pk=pk, slug=postInstance.mainSlug.slug)
    print(postInstance.title)
    context={
        'post':postInstance,
    }
    return render(request, "blog/post.html", context)
def getUrlFromSlug(request, slug):
    postSlug = get_object_or_404(blogSlug, slug=slug)
    return redirect(postView, postSlug.parent.pk)
