from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "index.html", {})

def survey(request):
	return render(request, "Take_survey.html", {})