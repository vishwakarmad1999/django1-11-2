import random
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Function based views
def home(request):
	# return HttpResponse(html_) | {} -> context
	num = random.randint(0, 1000)

	context = {"lang" : "Python, yes...", 
				"num" : num, 
				"bool_item" : True,
				"list" : list(range(num))}

	return render(request, "base.html", context)

def about(request):
	return render(request, "about.html", {})