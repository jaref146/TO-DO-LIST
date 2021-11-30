from django.shortcuts import render, HttpResponse, redirect
from .forms import edit_order_detail
from .models import Todo
import datetime
# Create your views here.

def index(request):
    tasks = Todo.objects.all()
    contex = {
        'tasks':tasks
              }
    return render(request, 'index.html', contex)

def update(request, update_pk):
    tasks_row = Todo.objects.get(id=update_pk)
    fo_edit_order_detail = edit_order_detail(instance=tasks_row)
    contex = {
        'fo_edit_order_detail':fo_edit_order_detail,
        'tasks_row':tasks_row,
              }
    return render(request, 'update.html', contex)

def delete(request, delete_pk):
    tasks_row = Todo.objects.get(id=delete_pk)
    contex = {
        'tasks_row': tasks_row,
    }
    return render(request, 'delete.html', contex)

def deleted_data(request, deleted_data_pk):
    tasks_row = Todo.objects.get(id=deleted_data_pk)
    tasks_row.delete()
    return redirect('index')

def add(request):
    taking_task_name = request.POST.get('taking_task_name')
    var_Todo = Todo(task_name = taking_task_name, completed = False, update_date_at = None)
    var_Todo.save()
    return redirect('index')

def completed(request, pk):
    tasks_row = Todo.objects.get(id=pk)
    tasks_row.completed=True
    tasks_row.save()
    return redirect('index')

def updated_data(request):
    update_task_name = request.POST.get('update_task_name')
    tasks_row_id = request.POST.get('tasks_row_id')
    get_TODO = Todo.objects.get(id=tasks_row_id)
    get_TODO_nam = get_TODO.task_name
    get_TODO_tim = get_TODO.created_at

    fo_edit_order_detail = edit_order_detail(request.POST, instance=get_TODO)

    if fo_edit_order_detail.is_valid():
        savother_data = fo_edit_order_detail.save(commit=False)
        savother_data.task_name = update_task_name
        savother_data.created_at = get_TODO_tim
        savother_data.update_date_at = datetime.datetime.now()
        savother_data.save()
    return redirect('index')
