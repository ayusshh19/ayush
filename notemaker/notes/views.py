from django.contrib import  messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from matplotlib import use

from notes.models import notesmaking
# print(dictid['userid'])
# Create your views here.
def homepage(request):
    notes=notesmaking.objects.all()
    return render(request,'index.html',{'note':notes})
    
def updateid(request):
    if request.method=='POST':
        id=request.POST.get('userid')
        note=notesmaking.objects.get(id=id)
        print(note.abouttask)
        print('ayush')
        return render(request,'index.html',{'notes':note})
    else:
        print('janhavi')
        notes=notesmaking.objects.all()
        return render(request,'index.html',{'note':notes})
        
def createform(request):
    if request.method=='POST':
        username=request.POST.get('username')
        task=request.POST.get('task')
        about=request.POST.get('about')
        obj=notesmaking(username=username,task=task,abouttask=about)
        obj.save()
        messages.success(request,'your task has been successfully submitted!!')
        print(messages)
        return render(request,'index.html')
    else:
        notes=notesmaking.objects.all()
        return render(request,'index.html',{'note':notes})
        
def updateform(request,id):
    if request.method=='POST':
        username=request.POST.get('username')
        task=request.POST.get('task')
        about=request.POST.get('abouttask')
        print(username,task,about)
        obj=notesmaking(id=id,username=username,task=task,abouttask=about)
        obj.save()
        messages.info(request,'your task has been updated successfully!!!')
        return render(request,'index.html')
    else:
        notes=notesmaking.objects.all()
        return render(request,'index.html',{'note':notes})
    
def deleteform(request,id):
    if request.method=='POST':
        obj=notesmaking(id=id)
        obj.delete()
        messages.error(request,'Deleted successfully!!!')
        return render(request,'index.html')
    else:
        notes=notesmaking.objects.all()
        return render(request,'index.html',{'note':notes})    
    
def setcookie(request):
    responce=render(request,'setcookie.html')
    responce.set_cookie('name','ayush',max_age=30)
    return responce

def getcookie(request):
    # name=request.COOKIES['name']
    name=request.COOKIES.get('name')
    return render(request,'getcookie.html',{'ayush':name})

def delcookie(request):
    responce=render(request,'delcookie.html')
    responce.delete_cookie('name')
    return responce