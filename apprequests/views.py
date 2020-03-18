from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def checkSlots(request):
    if request.method == "GET":
        
        print('answer : '+request.META['QUERY_STRING'])
        # add code here to check free slots
        
        slot_available_staus = True
        return HttpResponse(str(slot_available_staus))