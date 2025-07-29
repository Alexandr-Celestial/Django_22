from idlelib.autocomplete import ID_CHARS

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product
from catalog.services import get_products_from_category


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'home.html'

    def get_queryset(self):
        queryset = cache.get('products')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('products', queryset, 60 * 15)  # Кешируем данные на 15 минут
        return queryset

class CategoryProductsListView(ListView):
    model = Product
    template_name = 'product_list_category.html'

    def get_queryset(self):
        id_category = self.kwargs.get('pk')
        queryset = cache.get('cat_products_' + id_category)
        if not queryset:
            queryset = get_products_from_category(id_category)
            cache.set('cat_products_', + id_category, queryset, 60 * 15)  # Кешируем данные на 15 минут
        return queryset

class ProductContactsView(TemplateView):
    template_name = 'contacts.html'

@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'

    # def post(self, request, *args, **kwargs):
        # self.object = self.get_object()
        #
        # if self.request.user != self.object.owner and not self.request.user.has_perm('catalog.change_product'):
        #     return HttpResponseForbidden("У вас нет прав редактировать этот продукт.")
        # return super().post(request, *args, **kwargs)

    def get_form_class(self):
        user = self.request.user

        if user == self.object.owner:
            return ProductForm
        if user.groups.filter(name='Moderators').exists():
            return ProductForm
        raise PermissionDenied

    def get_success_url(self):
        """ Перенаправление на страницу созданного блога. """

        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.request.user != self.object.owner and not self.request.user.has_perm('catalog.change_product'):
            return HttpResponseForbidden("У вас нет прав редактировать этот продукт.")
        return super().post(request, *args, **kwargs)



