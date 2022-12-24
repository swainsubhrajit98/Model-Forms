from django.shortcuts import render
from App.forms import *
from django.http import HttpResponse
# Create your views here.
def Insert_Topic(request):
    form=TopicForm()
    d={'form':form}
    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('The data inserted in Topic model by ModelForms')
    return render(request,'Insert_Topic.html',d)


def Insert_Webpage(request):
    form = WebpageForm()
    d={'form':form}
    if request.method=='POST':
        form_data=WebpageForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('The data inserted in Webpage model by ModelForms')    
    return render(request, 'Insert_Webpage.html',d)


def Insert_Access(request):
    form=AccessRecordsForm()
    d={'form':form}
    if request.method=='POST':
        form_data=AccessRecordsForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('The data inserted in AccessRecords model by ModelForms')
    return render(request, 'Insert_Access.html',d)
