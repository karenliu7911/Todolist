from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

# Create your views here.

# CRUD


# R:Read
def todo_list(request):
    todos = Todo.objects.all().order_by(
        "-created",
        "-important",
    )  # order_by 排序，預設升序，加個負號(-)變降序
    print(todos)

    return render(request, "todos/list.html", {"todos": todos})


# D:刪除
def todo_delete(request, id):
    try:
        todo = Todo.objects.get(id=id)  # 第一個id是Todo裡面的id, 第二個id是外部給的id
        print(todo)
        todo.delete()
    except:
        print("無此ID")

    return redirect("todo-list")
    # 此todo-list不是指函式todo_list，是urls.py裡面的todo-list


# C:新增
def todo_create(request):

    if request.method == "POST":
        print(request.POST)
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            print("新增todo完成")
            return redirect("todo-list")

    return render(request, "todos/create.html", {"form": TodoForm()})


#
