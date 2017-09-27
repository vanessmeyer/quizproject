from django.shortcuts import render

# here is some testdata. This is a list with dictionaries within. 

quizzes = [
	{
		"quiz_number": 1,
		"name": "Klassiska böcker",
		"description": "Hur bra kan du dina Klassisker?"
	},
	{
		"quiz_number": 2,
		"name": "Största fotbollslagen",
		"description": "Kan du dina lag?"
	},
	{
		"quiz_number": 3,
		"name": "Världens mest kända hackare",
		"description": "Kan du din hackerhistoria?"
	},	
]

# Create your views here. These are view functions.
def startpage(request):
		context = {
			"quizzes": quizzes,
		}
		return render(request, "startpage.html", context)

def quiz(request, quiz_number):
	return render(request, "quiz.html")

def question(request, quiz_number, question_number):
	return render(request, "question.html")

def completed(request, quiz_number):
	return render(request, "completed.html")