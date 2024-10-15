from django.shortcuts import render
from .models import Subs

# Create your views here.


def tree(request):
    return render(request, 'treeemps/tree.html',{'subs':Subs.objects.all()})
