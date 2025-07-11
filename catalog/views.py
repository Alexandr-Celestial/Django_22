from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'home.html'

class ProductContactsView(TemplateView):
    template_name = 'contacts.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('catalog:home')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'

    def get_success_url(self):
        """ Перенаправление на страницу созданного блога. """

        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')



