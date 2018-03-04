import random
from acumen.models import Room
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def index(request):
	return HttpResponse("This is the Acumen home page, but you can go to these other places: <p><a href=/ian>Ian's page</a></p>")

# the ian and tara function are passing in roughly the same things tokens (with different values), 
# but the ian function is pulling from the database, while the tara function is using a class defined in this file
def ian(request):
	#essentially the "route tokens"
	rooms = Room.objects.all()
	context = {
	'middle_name':'james',
	'last_name':'bell',
	'rooms': rooms
	}
	return render(request,'ian.html',context)

def tara(request):
	#essentially the "route tokens"
	context = {
		'middle_name':'Alissa',
		'last_name':'Bell',
		'rooms': rooms
	}
	return render(request,'ian.html',context)

#First try at using a randomizer to determine which experience to serve. 
# In order to keep test integrity, we'll need to pass in a user ID/ test identifier with the request
# so that we can keep a user in a specific test. 
def acubox(request):
	#using this I can read the cookies associated with the request.
	print(request.COOKIES);
	selection = random.randrange(2)+1
	if selection == 1:
		return render(request,'acubox-a.js')
	elif selection == 2:
		return render(request,'acubox-b.js')

	

class iRoom:
	def __init__(self,owner,level,occupants):
		self.owner = owner
		self.level = level
		self.occupants = occupants

rooms = [
	iRoom('Master','Level 1', 2),
	iRoom('Jackson','Level 1', 1),
	iRoom('Lincoln','Basement',1),
	iRoom('Ayla','Baseent',1),
]
	