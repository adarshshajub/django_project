from django.shortcuts import render
from .models import Tree
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def tree(request,name):
    trees =Tree.objects.filter(search_link_key=name).values()
    if not trees:
        template = loader.get_template('details/error.html')
    else:
        template = loader.get_template('details/trees.html')
    context = {
        'tree': trees,
    }
    return HttpResponse(template.render(context, request))


def author_admin(request):
    return render(request,"details/author-login.html")