from django.db import models

class Question(models.Model):
    #contains the prose of the question
    question = models.CharField(max_length=2000)
    #what topic the question is about 
    topic = models.CharField(max_length=200)
    #pre-filled code 
    question_code = models.CharField(max_length=2000)
    #code that the user inputs
    answer_code = models.CharField(max_length=2000)

class Test(models.Model):
	#there can be multiple tests per question
	question = models.ForeignKey(Question)
	#holds the code for the tests
	test_code = models.CharField(max_length=2000)    
