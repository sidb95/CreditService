from django.shortcuts import render, redirect
from .models import Person, Session


class Authenticator():
  
  def __init__(self, usr):
    self.usr = usr
  
  def authenticate(self, password):
    session = Session.objects.get(uuid=self.usr.uuid)
    if (password == usr.password): # type: ignore
      if session is None or session is "":
        return ""
      else:
        return session.sid


def get_params(request, keys):
  params = {}
  for key in keys:
    params[key] = request.POST[key]
  return params


def index(request):
  if request.method == "GET":
    return render(request, "Authenticator/index.html")
  else:
    params = get_params(request, ['name', 'email', 'annual_income', 'password'])
    usr = Person.objects.create(name=params["name"], email=params["email"], 
                                annual_income=params["annual_income"], 
                                password=params["password"])
    usr.save()
    return redirect("Authenticator:login")


def login(request):
  if request.method == "GET":
    return render("Authenticator:login")
  else:
    params = get_params(request, ['email', 'passsword'])
    usr = Person.objects.get(email = params["email"])
    auth = Authenticator(usr)
    session_id = auth.authenticate(params["password"])
    if session_id != "":
      context = {"sid": session_id}
      return redirect("Welcome:index", context)
    else:
      context = {"messages": ["failed to authenticate"]}
      return render("Authenticator/login.html", context)
