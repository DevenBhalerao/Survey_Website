from django.shortcuts import render
from .models import Choice,Question
from .forms import SurveyForm
# Create your views here.

def index(request):
	return render(request, "index.html", {})

def survey(request):
	form = SurveyForm()
	question_objects = Question.objects.all()
	print(question_objects)
	choice_objects = Choice.objects.all()
	context = {
		"questions" : question_objects,
		"choices" : choice_objects,
		"form" : form
	}
	return render(request, "Take_survey.html", context)

def vote(request):
	print request.POST
	user_choice_list = list()
	choice_objects = list()
	default_choices = Choice.objects.all()
	for x in range(1, len(Question.objects.all())+1):
	    choice = "choice"+str(x)
	    choice_objects.append(Choice.objects.get(pk=request.POST[choice]))
	print choice_objects
	for choice in choice_objects:
		choice.votes += 1
		choice.save()
	context = {
	    "Question" : Question.objects.all(),
		"Choices" : Choice.objects.all()
	}
	return render(request, "results.html", context)	