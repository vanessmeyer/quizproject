from django.shortcuts import render
#This import pulls in Quiz models so we can connect views to database data
from quiz.models import Quiz 
from django.shortcuts import redirect


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

#The question view definition needs to first identify which quiz these questiosn belong to so it can use the quiz_number that with the urls.py to question view. We use quiz.objects.get to get out the quiz from the database. 
#Then we save the quiz as a variable that we call quiz.
#Then we need to get out all the question from the list to a list by witting quiz.question.all().This will get out all the question that belong to that specific quiz.
# Then we use question_number, the number that comes with the question view, to get out the right "position" from the list of questions (i.e. each question has its own url).  

def question(request, quiz_number, question_number):
	quiz = Quiz.objects.get(quiz_number=quiz_number)
	questions = quiz.questions.all()
	question = questions[question_number - 1]
	context = {
		"question_number": question_number,
		"question": question.question,
		"answer1": question.answer1,
		"answer2": question.answer2,
		"answer3": question.answer3,
		"quiz": quiz,
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

# Here we define a new view (i.e. logic) for when a user answers to the quiz. This logic defines what we will do with those answers.
# The request.POST gets out the choice the user made to the question. 
# Then we get out the dictionary with all the user's answers so far and save the users latest answer to that list (i.e. saved_answers).
# We then save thier latest answer and connect to the question they answered (i.e. saved_answers connects to question_number) 
# Then we save the whole list with the questions the user has answered. 
# Finally, we redirect the user to the next question by taking the question we are on (i.e. question_page) and adding 1 (i.e +1) to the question_number
def answer(request, quiz_number, question_number):
	answer = request.POST["answer"]
	saved_answer = request.session.get(str(quiz_number), {})
	saved_answers[question_number] = int(answer)
	request.session[quiz_number] = saved_answers
	return redirect("question_page", quiz_number, question_number + 1)
