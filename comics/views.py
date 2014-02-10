from comics.models import Book
from django.views.generic import TemplateView


class CatalogView(TemplateView):
    template_name = "comics/catalog.html"

    def get_context_data(self, **kwargs):
        return {
            'books': Book.objects.all()
        }