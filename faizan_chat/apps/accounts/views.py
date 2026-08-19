from django.shortcuts import render
from django.contrib.auth.models import user

# Create your views here.
def home(request):
    return render(request, "accounts/accounts.html")
