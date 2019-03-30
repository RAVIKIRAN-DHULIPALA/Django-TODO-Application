from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import TodoItem

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request,'todo.html',
    {'alltodo':all_todo_items})

def addTodo(request):
    TodoItem(content = request.POST['content']).save()
    return HttpResponseRedirect('/todo/')

def delete_Todo(request):
    item_to_delete = TodoItem.objects.get(id=str(request).split('/')[2])
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')


