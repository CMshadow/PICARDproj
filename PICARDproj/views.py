from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User, Group

def TestPage(request):
    if request.user.groups.all()[0].name == 'Patient':
        return render(request,'patient_dashboard.html')
    if request.user.groups.all()[0].name == 'Physician':
        return render(request,'physician_dashboard.html')
    if request.user.groups.all()[0].name == 'Caregiver':
        return render(request,'caregiver_dashboard.html')


def ThanksPage(request):
    return render(request,'thanks.html')

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)

def ourstory(request):
	return render(request,'ourstory.html')

def aboutpicard(request):
	return render(request,'aboutpicard.html')
