from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blogs.models import Blog


# Create your views here.

class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(sign_publication=True)


class BlogCreateView(CreateView):
    model = Blog
    fields = '__all__'
    success_url = reverse_lazy('blogs:blogs')

class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.count_view += 1
        obj.save()
        return obj


class BlogUpdateView(UpdateView):
    model = Blog
    fields = '__all__'

    def get_success_url(self):
        """ Перенаправление на страницу созданного блога. """

        return reverse("blogs:detail_blogs", args=[self.kwargs.get("pk")])

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:blogs')
