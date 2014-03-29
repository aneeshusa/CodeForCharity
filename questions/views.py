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
	#gets the next topic id and info 
	next_topic_id = int(topic_id) + 1
	next_topic_text = Topic.objects.get(pk=topic_id).topic
 	#if there are no more topics, go to finish
 	if next_topic_text == topic.topic:
		next_topic_id = 'finish'
		next_topic_text = 'finish'
	print next_topic_id
	print next_topic_text
	#gets the questions associated with that topic 
	question_list = topic.question_set.all()
	template = loader.get_template('questions/detail.html')
	context = RequestContext(request, {
	    'question_list': question_list,
	    'topic': topic.topic,
	    'next_topic_id': next_topic_id,
	    'next_topic_text': next_topic_text,
	})
	return HttpResponse(template.render(context))

def finish(request):
	return HttpResponse("Thank you for playing!")
