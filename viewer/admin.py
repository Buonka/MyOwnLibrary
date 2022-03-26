from django.contrib.admin import ModelAdmin


class BookAdmin(ModelAdmin):
    @staticmethod
    def released_year(obj):
        return obj.released.year

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description='')


class AuthorAdmin(ModelAdmin):
    @staticmethod
    def genre_name(obj):
        return obj.name.lower()


class GenreAdmin(ModelAdmin):
    @staticmethod
    def genre_name(obj):
        return obj.name.lower()
