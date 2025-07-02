from django.views.generic import TemplateView, ListView, DetailView

from catalog.models import Product


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'home.html'

class ProductContactsView(TemplateView):
    template_name = 'contacts.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail_product'

