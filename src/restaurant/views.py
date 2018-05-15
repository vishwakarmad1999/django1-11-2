import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

# Function based views
def home(request):
	# return HttpResponse(html_) | {} -> context
	num = random.randint(0, 1000)

	context = {"lang" : "Python, yes...", 
				"num" : num, 
				"bool_item" : True,
				"list" : list(range(num))}

	return render(request, "home.html", context)

def about(request):
	return render(request, "about.html", {})

class ContactView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "contact.html", {})