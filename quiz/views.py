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

# Why the quiz_number -1? Because quizzes is a list and therefore quiz #1 is the first one in the list (i.e. place 0)
def quiz(request, quiz_number):
	context = {
		"quiz": quizzes[quiz_number - 1],
		"quiz_number" : quiz_number,
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
	return render(request, "completed.html")