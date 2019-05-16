
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def index(request, id):
    ls = ToDoList.objects.get(id=id)

    if request.method == "POST":
        print(request.POST)
        if request.POST.get("save"):
            for item in ls.item_set.all():
                if request.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()

        elif request.POST.get("newItem"):
            txt = request.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")

    return render(request, "list.html", {"ls":ls})

# def by_name(request, name):
#     ls = ToDoList.objects.get(name=name)
#     print("ToDoList.objects.get======", ls)
#
#     item = ls.item_set.get(id=2)
#     print("ls.item_set.get==", item)
#
#     return HttpResponse("<h1>%s</h1><br><p>%s</p>" %(ls.name, str(item.text)))

def base(request, id):
    ls = ToDoList.objects.get(id=id)
    return render(request, "list.html", {"ls":ls})

def home(request):
    return render(request, "home.html", {"name":"test"})

def create(request):
    if request.method =="POST":
        form = CreateNewList(request.POST)

        if form.is_valid():

            n = form.cleaned_data["name"]
            print(ToDoList.objects.all())
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(request, "create.html", {"form":form})







