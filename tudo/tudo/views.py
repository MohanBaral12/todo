from django.db.models import Model
from django.http import HttpResponse
from django.shortcuts import *
from tudo.models import tudo
from datetime import datetime
from django.db import models



# index page is called by url.py
def random(request):
    now = datetime.now()

    current_date = now.date()     # Only date (YYYY-MM-DD)
    current_time = now.strftime("%H:%M:%S")      # Only time (HH:MM:SS.microseconds)

    return HttpResponse(f"<h1>Date is: {current_date} <br> Time is: {current_time}"
                        f"<br>Date and time is {datetime.now()}</h1>")






def index(request):
    print("index page is called! ")
    return render(request,"navbar.html",{})





def update(request, id):
    now = datetime.now()
    task = tudo.objects.get(pk=id)
    if request.method == 'POST':
        #Fatch the data.
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.dueDate = request.POST.get('dueDate')

        #Put the value in Database.
        t=tudo()
        t.title=task.title
        t.description=task.description
        t.date=task.dueDate
        t.last_update=datetime.now()          # Only date (YYYY-MM-DD)
        task.save()
        return redirect('/view-task/')
    return render(request, "update.html", {'t': task})





def view_task(request):
    tasks = tudo.objects.filter(completed=False).order_by('-last_update')
    return render(request, "view_task.html", {"tudo": tasks})




# home page is called by url.py
def home(request):
    print("Home page is called! ")
    return render(request,"home.html",{})




# add task is called by url.py
def add_task(request):
    date=datetime.now()

    if request.method=='POST':
        if request.POST.get('title')=='' and request.POST.get('description')=='' and request.POST.get('dueDate')=='':
            return render(request,'add_task.html',{'error': True})
        print("Task Add page called")
        # Fetch data from form.
        title=request.POST.get('title')
        description=request.POST.get('description')
        dual_date=request.POST.get('dueDate')

    #     Create table and send data.
        now = datetime.now()
        t=tudo()
        t.title=title
        t.description=description
        t.date=dual_date
        t.last_update=now.date()
        t.save()
        return redirect('/home/')
    return render(request,"add_task.html",{})




def delete(request, id):
    tudo_list=tudo.objects.get(pk=id)
    tudo_list.delete()
    return redirect('/view-task/')



def complete_task(request, id):
    task = tudo.objects.get(pk=id)
    task.completed = True
    task.save()
    return redirect('/completed-tasks/')  # or wherever you want to go after completion




def complete(request):
    task = tudo.objects.get(pk=id)
    task.completed = True
    task.save()
    completed_tasks = tudo.objects.filter(completed=True).order_by('-last_update')
    return render(request, 'complete_task.html', {'tudo': completed_tasks})




def completed_tasks(request):
    completed = tudo.objects.filter(completed=True).order_by('-last_update')
    return render(request, 'complete_task.html', {'tudo': completed})

