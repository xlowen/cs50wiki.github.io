import random
from django.shortcuts import render
from django import forms
from . import util

class NewTaskForm(forms.Form):
    Title = forms.CharField(label="New entry title:")
    Content = forms.CharField(widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def showentry(request, title):
    etitle = util.get_entry(title)
    print(title)
    if etitle != None:
        return render(request, "wiki/entry.html", {
        "etitle": etitle
    })
    else:
        return render(request, "wiki/entry.html", {
            "title": title
        })
    
def new(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            Title = form.cleaned_data["Title"]
            Content = form.cleaned_data["Content"]
            util.save_entry(Title, Content)
            print("file is saved.")
        else:
            return render(request, "encyclopedia/new.html", {
                "form": form
            })

    return render(request, "encyclopedia/new.html", {
        "form": NewTaskForm()
    })

def result(request):
    req = request.GET['q'].lower()
    entries = util.lowentry(util.list_entries())
    result = [entry for entry in entries if req in entry]
    print(req)
    
    if req == "":
        print("entered null")
        rentry = random.choice(util.list_entries())     
        return render(request, "encyclopedia/result.html", {
        "empty": req,
        "rentry": rentry
    })
    elif req.lower() in entries:
        print("entered entryfound")
        etitle = util.get_entry(req)
        return render(request, "wiki/entry.html",{
            "etitle": etitle
        })
    elif result:
        return render(request, "encyclopedia/result.html", {
            "req": req,
            "results": result
        })
        
    else:
        print("entered no if")
        return render(request, "encyclopedia/result.html",{
        "req": req
        })
