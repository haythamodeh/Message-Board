from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# errors = authors.objects.basic_validator(request.POST)

#     if len(errors) > 0:
#         for key,value in errors.items():
#             messages.error(request, value)
#         return redirect("/authors")
#     else:
#         if request.method == "POST":

# Create your views here.
def index(request):
    all_users = Users.objects.all()
    content = {
        "users": all_users
    }
    return render(request, "log_in_app/index.html", content)

def success(request):
    if not "loggedin" in request.session or request.session["loggedin"] != True:
        messages.error(request, "Please Log in first")
        return redirect("/")
    else:
        user = Users.objects.get(id = request.session["loggedinuser"])
        msg = Messages.objects.all().order_by("-created_at")
        comment = Comments.objects.all().order_by("-created_at")
        content ={
            "user": user,
            "messageObject": msg,
            "comments": comment
        }
        return render(request, "log_in_app/success.html", content)

def registerProcess(request):
    errors = Users.objects.basic_validator(request.POST)

    firstNameFromForm = request.POST["firstName"]
    lastNameFromForm = request.POST["lastName"]
    emailFromForm = request.POST["email"]
    passwordFromForm = request.POST["pw"]
    confirmpasswordFromForm = request.POST["confirmpassword"]
    
    if Users.objects.filter(email = emailFromForm):
        messages.error(request, "Email has been taken", extra_tags = "registerform")
        return redirect("/")
    if passwordFromForm != confirmpasswordFromForm:
        messages.error(request, "Passwords don't match", extra_tags = "registerform")
        return redirect("/")
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value, extra_tags = "registerform")
        return redirect("/")
    else:
        if request.method == "POST":
            pw_hash = bcrypt.hashpw(passwordFromForm.encode(), bcrypt.gensalt())
            Users.objects.create(firstName = firstNameFromForm, lastName = lastNameFromForm, email = emailFromForm, pw = pw_hash)
            user = Users.objects.last()
            request.session["loggedinuser"] = user.id
            request.session["loggedin"] = True
            messages.success(request, "Succesfully Registered", extra_tags = "success")
        return redirect(("/success"))


def loginProcess(request):
    if request.method == "POST":
        passwordlogin = request.POST["passwordlogin"]
        user = Users.objects.filter(email = request.POST["emaillogin"])
        print(user)
        
        if user:
            user = Users.objects.get(email = request.POST["emaillogin"])
            if bcrypt.checkpw(passwordlogin.encode(), user.pw.encode()):
                messages.success(request, "Succesfully Logged In", extra_tags = "success")
                request.session["loggedinuser"] = user.id
                request.session["loggedin"] = True
                print("*" *34)
                return redirect("/success")
            else:
                messages.error(request, "Incorrect Information!", extra_tags = "loginform")
                return redirect("/")
        else:
            messages.error(request, "Incorrect Information!", extra_tags = "loginform")
            return redirect("/")
    else:
        return redirect("/")


def logout(request):
    request.session.flush()
    messages.success(request, "Succesfully logged out!", extra_tags = "success")
    return redirect("/")



def postMessageProcess(request):
    msg = request.POST["message"]
    user = Users.objects.get(id = request.session["loggedinuser"])
    message = Messages.objects.create(msg = msg)
    message.users.add(user)
    return redirect("/success")


def postCommentProcess(request):
    comment = request.POST["comment"]
    user = Users.objects.get(id = request.session["loggedinuser"])
    msg = Messages.objects.get(id = request.POST["msg_id"])
    comment = msg.comments.create(comment = comment)
    comment.users.add(user)
    return redirect("/success")
