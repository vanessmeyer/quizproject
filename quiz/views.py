from django.shortcuts import render
#This command pulls in Quiz models so we can connect views to database data
from quiz.models import Quiz


# Create your views here. These are view functions.
def startpage(request):
		context = {
			"quizzes": Quiz.objects.all(),
		}
		return render(request, "startpage.html", context)

# Why the quiz_number -1? Because quizzes is a list and therefore quiz #1 is the first one in the list (i.e. place 0)
def quiz(request, quiz_number):
	context = {
		"quiz": Quiz.objects.get(quiz_number=quiz_number),
		"quiz_number": quiz_number,
	}
	return render(request, "quiz.html", context)

def question(request, quiz_number, question_number):
	context = {
		"question_number": question_number,
		"question": "Hur många bultar har ölandsbron?",
		"answer1": "12",
		"answer2": "66 400",
		"answer3": "7 428 954",
		"quiz_number": quiz_number,
	}
	return render(request, "question.html", context)

def completed(request, quiz_number):
	context = {
		"correct": 12,
		"total": 20,
		"quiz_number": quiz_number,
	}
	return render(request, "completed.html", context)
