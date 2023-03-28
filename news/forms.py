from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Назва статті',
                'class': "form-control",
            }),
            'anons': TextInput(attrs={
                'placeholder': 'Анонс статті',
                'class': "form-control",
            }),
            'full_text': Textarea(attrs={
                'placeholder': 'Текст статті',
                'class': "form-control",
            }),
            'date': DateTimeInput(attrs={
                'placeholder': 'Дата статті',
                'class': "form-control",
            })
        }