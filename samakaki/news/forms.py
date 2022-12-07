from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class ArticlesFrom(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'preview', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nazwa artykułu'
            }),
            'preview': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ogłoszenie'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tekst artykułu'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Data publikacji'
            }),
        }