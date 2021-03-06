# Create your views here.

from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from Feedback.models import Response
from PhonePeti.models import Call
from django.core.paginator import *

def index(request):
	return render_to_response('index.html', {'user': request.user})

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')

def feedbacks(request):
    all_feedbacks = Response.objects.all().order_by('-id')
    paginator = Paginator(all_feedbacks, 20)
    page = request.GET.get('page')
    try:
        all_feedbacks = paginator.page(page)
    except PageNotAnInteger:
        all_feedbacks=paginator.page(1)
    except EmptyPage:
        all_feedbacks = paginator.page(paginator.num_pages)
    return render_to_response('feedbacks.html', {'all_feedbacks': all_feedbacks})

def del_caller(request, callid):
	Call.objects.filter(id=callid).update(caller='')
	return redirect ('/')

def del_feedback(request, feedid):
	del_feed = Response.objects.get(id=feedid)
	del_feed.delete()
	return redirect ('/')

