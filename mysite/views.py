from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse

from .models import User
from .forms import LoginForm

class LoginAPIView(View):
    def get(self, request):

        if request.session.get("is_authenticated"):
            return HttpResponseRedirect(reverse("profile"))
        
        # create form instance
        login_form = LoginForm()

        # render page
        return render(request, "mysite/login.html", {
            "login_form": login_form,
            "is_valid": True
        })
    
    def post(self, request):

        # get email and password from request post
        email = request.POST["email"]
        password = request.POST["password"]

        # validate it form db
        get_user_details = User.objects.filter(email=email, password=password)

        # if true, call homepage
        # if false, call login pageagain
        if get_user_details.exists():
            request.session["is_authenticated"]=True
            return HttpResponseRedirect(reverse("profile"))
        else:
            return render(request, "mysite/login.html", {
                "login_form": LoginForm(request.POST),
                "is_valid": False
            })


def logout(request):
    request.session["is_authenticated"]=False
    return HttpResponseRedirect(reverse("login"))

def index(request):
    if request.session.get("is_authenticated"):
        return render(request, "mysite/profile.html")
    else:
        return HttpResponseRedirect(reverse("login"))
