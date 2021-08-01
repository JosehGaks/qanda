from django import forms
from django.conf import settings
from myapp.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'description', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'description': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)

        try:
            settings.QA_SETTINGS['qa_description_optional']
            self.fields['description'].required = not settings.QA_SETTINGS[
                'qa_description_optional']

        except KeyError:
            pass
