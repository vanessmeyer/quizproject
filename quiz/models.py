from django.db import models

# Create your models here. Models are How the site speaks to database.
class Quiz(models.Model):
		quiz_number = models.PositiveIntegerField()
		name = models.CharField(max_length=200)
		description = models.TextField()

		def __str__(self):
			return self.name

class Question(models.Model):
		question = models.TextField()
		answer1 = models.CharField(max_length=200)
		answer2 = models.CharField(max_length=200)
		answer3 = models.CharField(max_length=200)
		correct = models.PositiveIntegerField()
		# This last line makes its so that if a quiz is deleted so are the questions for that quiz. 
		quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE)

		def __str__(self):
			return self.quiz.name + " / " + self.question




