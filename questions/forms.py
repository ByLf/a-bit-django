from django import forms

from question.models import Author, Article


class AuthorForm(forms.Form):
    name = forms.CharField(max_length=255)
    birthday = forms.DateField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data['name']
        if name == 'asd':
            raise forms.ValidationError("It is invalid")
        return name

    def save(self):
        Author.objects.create(**self.cleaned_data)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title', 'date_published', 'is_published',
            'text', 'author', 'likes', 'picture'
        ]
