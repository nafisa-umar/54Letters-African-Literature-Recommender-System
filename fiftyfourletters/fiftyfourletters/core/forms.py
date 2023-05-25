from django import forms
from .models import Book
from django.utils.translation import gettext_lazy as _
from ckeditor.widgets import CKEditorWidget

import re


class BookForm(forms.Form):
    class meta:
        model = Book
        fields = '__all__'
