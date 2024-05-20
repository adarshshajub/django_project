from django.shortcuts import render
from django.http import HttpResponse
from details.models import Tree
from django.template import loader
# Create your views here.

def home(request):
    trees =Tree.objects.all()
    template = loader.get_template('home/index.html')
    context = {
        'tree': trees,
    }
    return HttpResponse(template.render(context, request))


# def tree_deatils(request,name):
#     trees =Tree.objects.filter(search_link_key=name).values()
#     if not trees:
#         template = loader.get_template('details/error.html')
#     else:
#         template = loader.get_template('details/trees.html')
#     context = {
#         'tree': trees,
#     }
#     return HttpResponse(template.render(context, request))

def tree_deatils(request):
    if request.method == "POST":
        link_key = request.POST.get('link_key')
        # link_key="mango"
        print(link_key)
        trees =Tree.objects.filter(search_link_key=link_key).values()
        if not trees:
            template = loader.get_template('details/error.html')
        else:
            template = loader.get_template('details/trees.html')
        context = {
            'tree': trees,
        }
    return HttpResponse(template.render(context, request))


