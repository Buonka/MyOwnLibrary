from django.urls import path

from viewer.views import BookView, BookDetailView

app_name = 'viewer'
urlpatterns = [
    path('book/', BookView.as_view(), name='book'),
    path('book/<int:pk>', BookDetailView.as_view(), name='read_book'),
]