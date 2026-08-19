from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    users = User.objects.all()
    return render(request, "accounts/accounts.html", {"users": users})
