from logging import getLogger

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView

from viewer.forms import AuthorForm
from viewer.models import Book, Author

LOG = getLogger()


class HomeView(TemplateView):
    template_name = 'home.html'


class BookView(ListView):
    template_name = 'book.html'
    model = Book


class AuthorView(ListView):
    template_name = 'author.html'
    model = Author


class BookDetailView(DetailView):
    template_name = 'book_detail_view.html'
    model = Book


class AuthorDetailView(DetailView):
    template_name = 'author_detail_view.html'
    model = Author


class AuthorCreateView(FormView):
    template_name = 'forms/form.html'
    form_class = AuthorForm
    success_url = reverse_lazy('viewer:create_author')
    permission_required = 'viewer.add_author'

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Author.objects.create(
            name=cleaned_data['author'],
        )
        return result
