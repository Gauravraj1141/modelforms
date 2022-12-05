from django.shortcuts import render
from .forms import showforms
from .models import mfforms


# Create your views here.


def mfhome(request):
    if request.method == "POST":
        data = showforms(request.POST)
        if data.is_valid():
            print("validate")
            nm = data.cleaned_data["name"]
            ct = data.cleaned_data["catagory"]
            vl = data.cleaned_data["village"]
            mydata = mfforms(name=nm, catagory=ct, village=vl)
            mydata.save()
    else:
        data = showforms()
    return render(request, "home/mf.html", {"forms": data})
