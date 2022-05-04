from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import Candidateform
from .models import Candidate

def home(request):
    cand=Candidate.objects.all()
    if request.method=="POST":
        form=Candidateform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        form=Candidateform()
    else:
        form=Candidateform()
    return render(request,'poll/home.html',{'form':form,'cand':cand})

def detail(request,pk):
    candidate=Candidate.objects.get(pk=pk)
    return render(request,'poll/details.html',{'candi':candidate})
  