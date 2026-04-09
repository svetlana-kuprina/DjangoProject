from django import forms
from django.template.defaultfilters import lower

from catalog.models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    FORBIDDEN_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    class Meta:
        model = Product
        fields = ["name", "description", "price", "category", "picture"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите название продукта"})
        self.fields["description"].widget.attrs.update({"class": "form-control", "placeholder": "Введите описание"})
        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите стоимость продукта"}
        )
        self.fields["category"].widget.attrs.update({"class": "form-control"})
        self.fields["picture"].widget.attrs.update({"class": "form-control"})

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < 0:
            raise ValidationError("Цена товара не может быть меньше 0")

        return price

    def clean_name(self):
        name = self.cleaned_data["name"]

        for for_word in self.FORBIDDEN_WORDS:
            if for_word in lower(name):
                raise ValidationError(
                    "Запрещено использовать слова казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар"
                )

        return name

    def clean_description(self):
        description = self.cleaned_data["description"]
        for for_word in self.FORBIDDEN_WORDS:
            if for_word in lower(description):
                raise ValidationError(
                    "Запрещено использовать слова казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар"
                )

        return description


class ProductModeratorForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ["publication"]
