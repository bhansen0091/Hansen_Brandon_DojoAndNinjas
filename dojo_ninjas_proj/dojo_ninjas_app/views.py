from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    context = {
        "dojos": Dojo.objects.all(),
        "ninjas": Ninja.objects.all(),
    }
    return render(request, "index.html", context)

def create_dojo(request):
    Dojo.objects.create(
        name = request.POST['dojo_name'],
        city = request.POST['dojo_city'],
        state = request.POST['dojo_state'],
        desc = "A brief description"
    )
    return redirect("/")

def delete_dojo(request, dojo_id):
    print(Ninja.objects.filter(dojo=Dojo.objects.get(id=dojo_id)))
    Ninja.objects.filter(dojo=Dojo.objects.get(id=dojo_id)).delete()
    print(Ninja.objects.filter(dojo=Dojo.objects.get(id=dojo_id)))
    Dojo.objects.get(id=dojo_id).delete()
    return redirect("/")

def create_ninja(request):
    Ninja.objects.create(
        dojo = Dojo.objects.get(id = request.POST['dojo_select']),
        first_name = request.POST['ninja_first_name'],
        last_name = request.POST['ninja_last_name']
    )
    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect("/")
