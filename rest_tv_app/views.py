from django.shortcuts import render, redirect, HttpResponse 
from .models import Tv_show
from django.contrib import messages

# Create your views here.


def index(request):
    return redirect("/shows")

def shows(request):
    all_shows=Tv_show.objects.all()
    context ={
        "all_shows": all_shows,
    }

    return render(request, "shows.html", context)

def new(request):
    return render(request, "new.html")

def create(request):
    if request.method == "POST":
            
        errors = Tv_show.objects.basic_validator(request.POST)
       
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/new")
            
        title = request.POST['title']
        network = request.POST['network']
        start_date = request.POST['date']
        desc = request.POST['desc']

        if len(desc) == 0:
            Tv_show.objects.create(title=title, network=network, start_date = start_date)
        else:
            Tv_show.objects.create(title=title, network=network, start_date = start_date, desc=desc)

        
        redir = ''
        redir +="/shows/"
        redir +=str(Tv_show.objects.last().id)
    
        return redirect(redir)
        
    return redirect("/shows")

def show_data(request, render_id):

    show = Tv_show.objects.get(id=render_id)
    
    
    context = {
        "show": show
    }
    return render(request, "show_data.html", context)

def edit(request, render_id):
    show = Tv_show.objects.get(id=render_id)
    
    datestr=str(show.start_date)
    context = {
        "show": show,
        "datestr": datestr
    }
    return render(request, "edit.html", context)

def make_edit(request):
    if request.method == "POST":

        show_id =request.POST['show_id']
        show = Tv_show.objects.get(id=show_id)

        errors = Tv_show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/shows/edit/"+ show_id)


        
        show.title = request.POST['title']
        show.date = request.POST['date']
        show.network = request.POST['network']
        show.desc = request.POST['desc']
        show.save()
        
        redir = ''
        redir +="/shows/"
        redir +=str(show.id)
        return redirect(redir)
        
    return redirect("/shows")

def delete_confirm(request, render_id):
    show = Tv_show.objects.get(id=render_id)

    context={
        "show": show
    }
    return render(request, "delete_confirm.html", context)

def make_delete(request):
    show_id = request.POST['show_id']
    if request.method == "POST":
        show = Tv_show.objects.get(id=show_id)
        show.delete()
        return redirect("/shows")
    return redirect("/shows")