from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CatalogListView, CatalogDetailView, TemplateContactView


app_name = CatalogConfig.name


urlpatterns = [
    path("", CatalogListView.as_view(), name="home"),
    path("contacts/", TemplateContactView.as_view(), name="contacts"),
    path("product/<int:pk>/", CatalogDetailView.as_view(), name="product"),
]
