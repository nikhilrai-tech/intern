from django.shortcuts import render,HttpResponseRedirect,get_object_or_404,redirect
from . forms import tectstackforms,registrationpage,loginform
from . models import techstack
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required()
def gethome(request):
    fm=techstack.objects.all()
    return render(request,"home.html",{"fm":fm})

@login_required()
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
@login_required()
def deletetech(request,id):
    Techstack=get_object_or_404(techstack,class_id=id)
    print(techstack)
    Techstack.delete()
    return redirect('/post/')

def registration(request):
    if request.method=="POST":
        fm=registrationpage(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("login")

    fm=registrationpage()
    return render(request,"registration.html",{'fm':fm})

def registrationlogin(request):
    if request.method == "POST":
        fm = loginform(request.POST)
        if fm.is_valid():  # Ensure form validation
            un = fm.cleaned_data["username"]
            ps = fm.cleaned_data["password"]
            user = authenticate(request, username=un, password=ps)
            print(un, ps)
            if user:
                login(request, user)
                return HttpResponseRedirect("/save/")
    else:
        fm = loginform()

    return render(request, "login.html", {"fm": fm})

def userlogout(request):
    logout(request)
    return HttpResponseRedirect("/")