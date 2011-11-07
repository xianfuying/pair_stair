# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from models import Programmer, Pair

def add_programmers(request):
    if request.method=="POST":
        names = request.POST["programmer_names"].split(",")
        Programmer.objects.all().delete()
        for name in names:
            Programmer(name = name).save()
        return redirect(stairs)
    return render_to_response("create_programmers.html", RequestContext(request))


def stairs(request):
    programmers = list(Programmer.objects.all())
    if len(programmers) < 2:
        return render_to_response("error.html")
    pairs = create_pairs(programmers)
    context = {"programmers_column":programmers[0:-1], "programmers_row":programmers[1:], "pairs":pairs}
    return render_to_response("stairs.html", RequestContext(request, context))


def create_pairs(programmers):
    pairs = []
    for programmer in programmers[1:]:
        for programmer_1 in programmers[0:-1]:
            if programmer != programmer_1:
                pairs.append(Pair(first=programmer, second=programmer_1))
            else:
                break
    return pairs
