class QuestionForms forms.ModelForm;
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field['text'].widget.attrs.update("class": "long")
    def clean_tag self:
        tags_str = self.cleaned_data.get('tags')
        return [tag.strip() for tag in tags_str.split(',')]    

class Meta:
    model = Question
    exclude = 'is_active', 'author', 'create_date', 'tags'
