from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product
from config.settings import WRONG_WORDS


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        print(self._meta.fields)
        for field in self._meta.fields:
            self.fields[field].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            # Текст подсказки внутри поля
        })

    class Meta:
        model = Product
        fields = ['name', 'description', 'picture', 'category', 'price']

    def clean_price(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        if name in WRONG_WORDS or description in WRONG_WORDS:
            raise ValidationError('Название и описание не должны содержать не допустимые слова')
