from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Item

def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request,"home-page.html", context)

# Create your views here.
class HomeView(ListView):
    model = Item
    paginate_by = 10
    template_name = "home.html"

class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"