from django.shortcuts import render,HttpResponseRedirect,get_object_or_404,redirect
from . forms import tectstackforms
from . models import techstack
from django.contrib import messages
def gethome(request):
    fm=techstack.objects.all()
    return render(request,"home.html",{"fm":fm})

def home(request):
    if request.method=="POST":
        fm=tectstackforms(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("post")
    fm=tectstackforms()
    return render(request,"index.html",{"fm":fm})

# def updatedata(request,id):
#     Techstack=get_object_or_404(techstack,class_id=id)
#     if request.method=="POST":
#         fm=tectstackforms(request.POST,instance=Techstack)
#         if fm.is_valid():
#             fm.save()
#             messages.success(request, "Data updated successfully")
#             return HttpResponseRedirect("/")
        
#     fm=tectstackforms(instance=Techstack)
#     return render(request,"update.html",{"fm":fm})

def deletetech(request,id):
    Techstack=get_object_or_404(techstack,class_id=id)
    print(techstack)
    Techstack.delete()
    return redirect('/post/')



