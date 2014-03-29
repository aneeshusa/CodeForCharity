from django.http import Http404
from django.shortcuts import render
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from questions.models import Topic

def index(request):
	return render(request, 'questions/index.html', {})

def detail(request, topic_id):
	#gets the topic associated with the id number
	topic = Topic.objects.get(pk=topic_id)
	#gets the next topic id and info
	#if there are no more topics, go to finish
	try: 
		next_topic_id = int(topic_id) + 1
		next_topic_text = Topic.objects.get(pk=next_topic_id).topic
	except:
		next_topic_id = 'finish'
		next_topic_text = 'finish'
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

#creates new user
def create_user(request):
    if request.method == 'POST': # If the form has been submitted...
        form = UserCreationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            user = form.save()
            return HttpResponseRedirect('/questions/1/') # Redirect after POST
    else:
        form = UserCreationForm() # An unbound form

    return render(request, 'questions/create_user.html', {
        'form': form,
    })

#logs user into the app
def authenticate_user(request):
    if request.method == 'POST': # If the form has been submitted...
        form = AuthenticationForm(None, request.POST or None) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
        	login(request, form.get_user())
        	return HttpResponseRedirect('/questions/1/') # Redirect after POST
    else:
        form = AuthenticationForm() # An unbound form

    return render(request, 'questions/login.html', {
        'form': form,
    })

def finish(request):
	return HttpResponse("Thank you for playing!")
