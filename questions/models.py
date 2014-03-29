from django.db import models

class Topic(models.Model):
	#what topic the question is about 
    topic = models.CharField(max_length=200)
		
class Question(models.Model):
	#mulitple questions per topic
	topic = models.ForeignKey(Topic)
	#true if the question is a part of the project, false if generic question
	isproject = models.BooleanField()
    #contains the prose of the question
	text = models.CharField(max_length=2000)
    #pre-filled code 
	question_code = models.CharField(max_length=2000)
    #code that the user inputs
	answer_code = models.CharField(max_length=2000)

class Test(models.Model):
	#there can be multiple tests per question
	question = models.ForeignKey(Question)
	#holds the code for the tests
	test_code = models.CharField(max_length=2000)    
