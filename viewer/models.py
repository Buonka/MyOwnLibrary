from django.db.models import Model, CharField, ForeignKey, DO_NOTHING, DateField, TextField


class Genres(Model):
    type = CharField(max_length=128)

    def __str__(self):
        return f"{self.type}"


class Publishers(Model):
    firm = CharField(max_length=128)

    def __str__(self):
        return f"{self.firm}"


class Authors(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"


class Books(Model):
    title = CharField(max_length=128)
    genre = ForeignKey(Genres, on_delete=DO_NOTHING)
    publisher = ForeignKey(Publishers, on_delete=DO_NOTHING)
    author = ForeignKey(Authors, on_delete=DO_NOTHING)
    date_release = DateField()
    translation_by = CharField(max_length=128)
    description = TextField()

    def __str__(self):
        return f"{self.title}"

