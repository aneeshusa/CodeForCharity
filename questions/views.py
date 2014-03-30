from django.http import Http404
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from questions.models import Topic

def index(request):
	return render(request, 'questions/index.html', {})

#conatins all the questions 
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
            user.progress = 1; 
            user.score = 0; 
            user.save()
            print type(user)
            #login(request, user)
            return HttpResponseRedirect('/questions/login/') # Redirect after POST
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

#logs user out of app 
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/questions/login') # Redirect after POST

def update(request, topic_id):
    #make sure the request is coming from localhost
    #then we know that it's formatted nicely (200 and all)
    #post data format: {"username": "aneeshusa", "question_id": "23", "passed": "True"}
    # so just update the score in the django data base and send back the ajax response to the original request
    return HttpResponseRedirect('/questions/1/')



def verify(request, topic_id):
    print 'verify called' 
    if request.is_ajax():
        print 'HUZZAH!'
        data = {
            #stuff
        }
        myurl = '/questions/' + str(topic_id)
        return HttpResponseRedirect(myurl)
    else:
        myurl = '/questions/' + str(topic_id)
        return HttpResponseRedirect(myurl)
    
    #unpack post request and make sure it's in the correct format 
    #request.user <-- gets currently logged in user
    #get username
    #check that username has access to question they are submitting  
    #
    #send aneesh a post request 
    myurl = '/questions/' + str(topic_id)
    return HttpResponseRedirect(myurl)

#endpage
def finish(request):
	return HttpResponse("Thank you for playing!")
