from django.shortcuts import redirect, render
import random
from .models import Stupid,Fat,Dumb

# Create your views here.

def respond_to_websockets(message):
    """
    This function selects random joke from a list of mapped key of jokes dict 
    Return: joke
    """
    jokes = {
     'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
     'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
     'dumb':   ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""] 
     }  

    result_message = None
    #{
    #    'type': 'text'
    #}
    if message  == 'stupid' :
        result_message = random.choice(jokes['stupid'])
    
    elif message  == 'fat' :
        result_message = random.choice(jokes['fat'])
    
    elif message  == 'dumb' :
        result_message = random.choice(jokes['dumb'])

    #elif message['type'] in ['hi', 'hey', 'hello']:
    #    result_message['type'] = "Hello to you too! If you're interested in yo mama jokes, just tell me fat, stupid or dumb and i'll tell you an appropriate joke."
    else:
        result_message['type'] = "I don't know any responses for that. If you're interested in yo mama jokes tell me fat, stupid or dumb."

    return result_message

def home(request):
    """
    This function returns home page
    """
    return render(request,'actioncountapp/index.html')

def addcount(request):
    """
    This function returns joke page with a random joke of selected type
    """
    name = request.POST['keyword']
    if name == 'stupid':
        addstupid = Stupid.objects.create()
        #message = message_list.append(name)
        #message = {'text':message1}
        joke = respond_to_websockets(name)
        info = {'joke':joke,'name':name}
        return render(request,'actioncountapp/joke.html',context=info)
    
    elif name == 'fat':     # checking condition to render fat joke
        addstupid = Fat.objects.create() 
        joke = respond_to_websockets(name)
        info = {'joke':joke,'name':name}
        return render(request,'actioncountapp/joke.html',context=info)

    elif name == 'dumb':     # checking condition to render dumb joke
        addstupid = Dumb.objects.create() 
        joke = respond_to_websockets(name)
        info = {'joke':joke,'name':name}
        return render(request,'actioncountapp/joke.html',context=info)

    else:     # this is to say not found any joke
        joke = "There is no joke to match the keyword"
        info = {'joke':joke,'name':name}
        return render(request,'actioncountapp/joke.html',context=info)
    
def getcount(request):
    """
    This function returns count page with a counts of joke of selected type
    """
    name = request.POST['getcount']
    if name == 'stupid':
        joke = Stupid.objects.last()
        count_name =" Count Of " + name
        info = {'joke':joke,'name':count_name}
        return render(request,'actioncountapp/count.html',context=info)

    elif name == 'fat':
        joke = Fat.objects.last()
        count_name =" Count Of " + name
        info = {'joke':joke,'name':count_name}
        return render(request,'actioncountapp/count.html',context=info)
    
    elif name == 'dumb':
        joke = Dumb.objects.last()
        count_name =" Count Of " + name
        info = {'joke':joke,'name':count_name}
        return render(request,'actioncountapp/count.html',context=info)

    else:
        joke1 = str(Stupid.objects.last())
        joke2 = str(Fat.objects.last())
        joke3 = str(Dumb.objects.last())
        joke = joke1 + " , " + joke2 +  " & " + joke3 +  "."
        count_name =" Count Of " + name 
        info = {'joke':joke,'name':count_name}
        return render(request,'actioncountapp/count.html',context=info)
    
    
