from django.shortcuts import render
from .models import Choice,Question
# Create your views here.

def index(request):
	return render(request, "index.html", {})

def survey(request):
	question_objects = Question.objects.all()
	choice_objects = Choice.objects.all()
	context = {
		"questions":question_objects,
		"choices" :choice_objects
	}
	return render(request, "Take_survey.html", context)