from django.shortcuts import render
from .models import Produit
# Create your views here.
def index (request):
     return render(request, 'index.html')
def produits (request):
     return render(request, 'product.html')