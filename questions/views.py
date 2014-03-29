from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from questions.models import Topic

def index(request):
    return HttpResponse("Hello, world.")

def detail(request, topic_id):
	#gets the topic associated with the id number
	topic = Topic.objects.get(pk=topic_id)
	#gets the questions associated with that topic 
	question_list = topic.question_set.all()
	template = loader.get_template('questions/detail.html')
	context = RequestContext(request, {
	    'question_list': question_list,
	    'topic': topic.topic,
	})
	return HttpResponse(template.render(context))