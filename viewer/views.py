from logging import getLogger

from django.views.generic import TemplateView, ListView, DetailView

from viewer.models import Book

LOG = getLogger()


class HomeView(TemplateView):
    template_name = 'home.html'


class BookView(ListView):
    template_name = 'book.html'
    model = Book


class BookDetailView(DetailView):
    template_name = 'book_detail_view.html'
    model = Book
