import random
import markdown2
from django.shortcuts import render
from django.shortcuts import redirect
from django import forms
from . import util

class NewTaskForm(forms.Form):
    Title = forms.CharField(label="New entry title:", widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 80%'}))
    Content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control tasize', 'style': 'width: 80%; height: 300px'}))


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def showentry(request, title):
    atitle = util.get_entry(title)
    etitle = markdown2.markdown(atitle)
    if etitle != None:
        return render(request, "wiki/entry.html", {
        "etitle": etitle,
        "title": title
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
            exists = f"{Title}"
            if util.save_entry(Title, Content) == None:
                print("same name")
                return render(request, "encyclopedia/new.html", {
                    "exists": exists
                })
            else:
                print("accessed else")
                return redirect(f"wiki/{ Title }", {
                    "etitle": Title
                })                        
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
    print("isso é request.get:", request.GET)
    print("isso é req:", req)
    
    if req == "":
        print("entered null")
        rentry = random.choice(util.list_entries())     
        return render(request, "encyclopedia/result.html", {
        "empty": req,
        "rentry": rentry
    })
    elif req.lower() in entries:
        etitle = util.get_entry(req)
        print(etitle)
        return render(request, "wiki/entry.html",{
            "title": req,
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

def edit(request):

    
    class EditForm(forms.Form):
        Name = forms.CharField(widget=forms.HiddenInput)
        Current = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 80%; height: 300px;'}))

    if request.method == "GET":
        current = request.GET['title']
        form = EditForm(initial={'Current': util.fname(current), 'Name': current})
        print("1", util.fname(current))
        print("2", request.POST)
        print("3", current)
        print("4", form["Current"])
        print("5", request.GET)
 
        return render(request, "encyclopedia/edit.html",{
            "form": form
        })
          
    elif request.method == "POST":

        print("2", request.POST)
        current = request.POST['Name']
        print("3", current)
        form = EditForm(request.POST)
        if form.is_valid():
            Content = form.cleaned_data['Current']
            util.save_edit(current, Content)
            return redirect(f"wiki/{ current }", {
                "etitle": current
            })
        else: 
            return render(request, "encyclopedia/index.html")
    else:
        return render(request, f"encyclopedia/index.html")
    
def randompage(request):

    print(request)
    rentry = random.choice(util.list_entries())
    return redirect(f"wiki/{ rentry }", {
        "rentry" : rentry
    })