from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
from datetime import datetime, date

# Create your views here.
def mainView(request):
    all_items = TodoItem.objects.all()
    params = {'all_items': all_items}
    return render(request, 'todo/index.html', params)

def addTodo(request):
    title = request.POST.get('title', '')
    content = request.POST.get('content', '')

    if title is not "":
        a = TodoItem(title = title, content = content, date = date.today(), time = datetime.now())
        a.save()
        return HttpResponseRedirect('/todo')
    else:
        params = {'error': 'no title found.'}
        return render(request, 'todo/index.html',params)

def addTask(request):
    return render(request, 'todo/addTask.html')

def deleteTask(request, todo_id):
    print(todo_id)
    task = TodoItem.objects.get(id= todo_id)
    task.delete()
    return HttpResponseRedirect('/todo')