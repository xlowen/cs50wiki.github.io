import random
from django.shortcuts import render

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def showentry(request, title):
    etitle = util.get_entry(title)
    if etitle != None:
        return render(request, "wiki/entry.html", {
        "etitle": etitle
    })
    else:
        return render(request, "wiki/entry.html", {
            "title": title
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
        print(result)
        return render(request, "encyclopedia/result.html", {
            "req": req,
            "results": result
        })
        
    else:
        print("entered no if")
        return render(request, "encyclopedia/result.html",{
        "req": req
        })
