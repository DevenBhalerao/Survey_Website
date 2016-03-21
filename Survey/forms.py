from django import forms

from .models import Question,Choice

questions = Question.objects.all()
choices = Choice.objects.all()


class SurveyForm(forms.Form):
	choices = forms.ChoiceField(choices=[(obj.id, obj.choice_text) for obj in Choice.objects.all()], widget=forms.RadioSelect())
	class Meta:
		model = Choice
		fields = [
			"question"
			"choice"
		]