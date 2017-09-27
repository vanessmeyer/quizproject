from django.urls import path
from quiz import views

# this is a list. This list describes the url patterns/paths. The last part of the path references a python method (e.g. views.startpage references the python method def startpage).
urlpatterns = [
	path("", views.startpage, name="start_page"),
	path("quiz/<int:quiz_number>/", views.quiz, name="quiz_page"),
	path("quiz/<int:quiz_number>/question/<int:question_number>/", views.question, name="question_page"),
	path("quiz/<int:quiz_number>/completed/", views.completed, name="completed_page"),

]
