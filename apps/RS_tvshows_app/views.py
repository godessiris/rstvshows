from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

# Create your views here.

def index(request):
    return redirect('/shows')

def shows(request):
    all_shows = Show.objects.all()
    context ={
        'all_shows' : all_shows,
    }
    return render(request,"RS_tvshows_app/index.html", context)

def new_shows(request):
    return render(request,"RS_tvshows_app/create.html")
    

def process_create(request):
    errors=Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/shows/new')
    else:
        Show.objects.create(title=request.POST['title'], description=request.POST['description'],release_date=request.POST['release_date'],network=request.POST['network'] )
        show = Show.objects.last()
        return redirect(f"/shows/{show.id}")

def read_shows(request, show_id):
    show = Show.objects.get(id=show_id)
    context ={
        'show':show,
    }
    return render(request,"RS_tvshows_app/read.html", context)

def update_shows(request, show_id):
    show = Show.objects.get(id=show_id)
    context ={
        'show':show,
    }
    return render(request,"RS_tvshows_app/update.html", context)

def process_update(request, show_id):
    show = Show.objects.get(id=show_id)
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show.id}/edit')
    else:
        
        show.title= request.POST["title"]
        show.network = request.POST["network"]
        show.description = request.POST["description"]
        show.release_date= request.POST["release_date"]
        show.save()
        context = {
            'show':show,
            'show.title': show.title,
            'show.network':show.network,
            'show.description':show.description,
            'show.release_date': show.release_date,
        }
        messages.success(request, "Show successfully updated")
        return redirect(f"/shows/{show.id}", context)

def process_destroy(request, show_id):
    remove_show=Show.objects.get(id=show_id)
    remove_show.delete()
    return redirect('/shows')