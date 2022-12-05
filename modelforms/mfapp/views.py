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
            ct = data.cleaned_data["Email"]
            vl = data.cleaned_data["Address"]
            mydata = mfforms(name=nm, Email=ct, Address=vl)
            mydata.save()
    else:
        data = showforms()
    return render(request, "home/mf.html", {"forms": data})
