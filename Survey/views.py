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
	for x in range(1, len(Question.objects.all())+1):
	    choice = "choice"+str(x)
	    print request.POST.get(choice)
	context = {
		
	}
	return render(request, "results.html", context)	