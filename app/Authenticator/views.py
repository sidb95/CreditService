from django.shortcuts import render, redirect
from .models import Person, Session
from django.contrib import messages


class Authenticator():
  
  def __init__(self, usr):
    self.usr = usr
  
  def authenticate(self, password): 
    if self.usr.uuid is not None:
      session = Session.objects.get(uuid=self.usr)
      if (password == self.usr.password):
        if session is None or session.sid == "":
          return ""
        else:
          return session.sid
      else:
        return ""
    else:
      return ""    


def get_params(request, keys):
  params = {}
  for key in keys:
    params[key] = request.POST[key]
  return params


def index(request):
  if request.method == "GET":
    return render(request, 'Authenticator/index.html')
  else:
    params = get_params(request, ['name', 'email', 'annual_income', 'password'])
    uuid = len(Person.objects.all()) + 1
    usr = Person.objects.create(uuid=uuid, name=params["name"], email=params["email"], 
                                annual_income=params["annual_income"], 
                                password=params["password"])
    usr.save()
    sid = len(Session.objects.all()) + 1
    session = Session.objects.create(uuid=usr, sid=sid)
    session.save()
    return redirect("Authenticator:login")



def login(request):
  if request.method == "GET":
    return render(request, "Authenticator/login.html")
  else:
    params = get_params(request, ['email', 'password'])
    usr = Person.objects.get(email=params["email"])  
    auth = Authenticator(usr)
    session_id = auth.authenticate(params["password"])
    if session_id != "" and session_id is not None:
      context = {"sid": session_id}
      return redirect("Welcome:index")
    else:
      messages.info(request, 'Password incorrect')
      return render(request, "Authenticator/login.html")
