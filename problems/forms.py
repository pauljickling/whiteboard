from django.forms import ModelForm, Textarea

from .models import Answer


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer', 'language']
        widgets = {
            'answer': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class CorrectForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['correct']
