from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import simplejson
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from register import models
from register.models import Participant
import uuid

def index(request):

	return render_to_response('register/index.html', {},)


@csrf_exempt
def submit(request):
	
	data = request.POST.dict()
	if data['email']:
		try:
			participant = models.Participant(**data)
			participant.token = str(uuid.uuid1()).replace("-", "")[:16]
			participant.save()
			send_mail(
				'[cs4hs] Registration', # subject
				"""Pentru a finaliza inregistrarea dvs. la evenimentul Computer Science for High School,
Va rugam urmati link-ul de mai jos:

    http://194.102.62.87/confirm/%s/
""" % participant.token,
				'cs4hs@info.uvt.ro', # from 
		    	[participant.email],  # to
		    	fail_silently=False
	    	)
		except Exception as err:
			return HttpResponse(simplejson.dumps({"success": False}))			
	return HttpResponse(simplejson.dumps({"success": True}))


def confirm(request, token):

	print token
	print request.GET
	try:
		participant = Participant.objects.get(token=token)
	except Exception as err:
		raise Http404
	if participant and participant.confirmed is False:
		participant.confirmed = True
		participant.save()
		return HttpResponseRedirect("/done/")


	return HttpResponse(simplejson.dumps({"success": True}))


def done(request):

	return render_to_response('register/done.html', {},)