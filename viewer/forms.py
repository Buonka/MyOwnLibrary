
from django.forms import ModelForm, NumberInput, DateField

from viewer.models import Author, Book, Genre


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

    released = DateField(widget=NumberInput(attrs={'type': 'data'}))


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"
