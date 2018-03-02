from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse('This is the Acumen home page')

def ian(request):
	#essentially the "route tokens"
	context = {
	'middle_name':'james',
	'last_name':'bell',
	'rooms':rooms
	}
	return render(request,'ian.html',context)

class Room:
	def __init__(self,owner,level,occupants):
		self.owner = owner
		self.level = level
		self.occupants = occupants

rooms = [
	Room('Master','Level 1', 2),
	Room('Jackson','Level 1', 1),
	Room('Lincoln','Basement',1),
	Room('Ayla','Baseent',1),
]
	