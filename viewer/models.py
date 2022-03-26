from django.db.models import Model, CharField, ForeignKey, DO_NOTHING, DateField, TextField


class Genre(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"


class Author(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"


class Book(Model):
    title = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    publisher = CharField(max_length=128)
    author = ForeignKey(Author, on_delete=DO_NOTHING)
    release_date = DateField()
    translation_by = CharField(max_length=128, blank=True)
    description = TextField()

    def __str__(self):
        return f"{self.title}"

