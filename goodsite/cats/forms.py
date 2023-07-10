from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Cats
        # fields = '__all__'
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    # user's validator starts with 'clean' and then field for validation
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 10:
            raise ValidationError('The name is longer than 10 characters')
        return title


    # title = forms.CharField(max_length=255, label='Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # slug = forms.SlugField(max_length=255, label='URL')
    # content = forms.CharField(label='Content', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    # is_published = forms.BooleanField(label='Publication', required=False, initial=True)
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Categories')
