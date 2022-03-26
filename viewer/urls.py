from django.urls import path

from viewer.views import BookView, BookDetailView, AuthorView, AuthorDetailView, AuthorCreateView, GenreView, \
    BookCreateView

app_name = 'viewer'
urlpatterns = [
    path('book/', BookView.as_view(), name='book'),
    path('author/', AuthorView.as_view(), name='author'),
    path('genre/', GenreView.as_view(), name='genre'),
    path('book/<int:pk>', BookDetailView.as_view(), name='read_book'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='read_author'),
    path('create_author/', AuthorCreateView.as_view(), name='create_author'),
    path('create_book/', BookCreateView.as_view(), name='create_book'),
]