from django.shortcuts import render
from .models import *
# Create your views here.
def Home(request):
    c=Category.objects.all()
    p=Product.objects.all()
    context={
        "category":c,
        "mahsulot":p
    }
    return render(request,"index.html",context)