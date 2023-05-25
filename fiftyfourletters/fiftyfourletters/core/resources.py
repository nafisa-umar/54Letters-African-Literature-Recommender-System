from import_export import resources
from .models import Book


class BookResource(resources.ModelResource):
    class meta:
        model = Book
