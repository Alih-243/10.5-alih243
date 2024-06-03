from django.shortcuts import render
from datetime import datetime

# Create your views here.

def home(r):
    d = {
        'lst': ['python', 'is', 'fun'],
        'time': datetime.now(),
        'empty': "",
    }
    return render(r, 'home.html', d)
def about(r):
    return render(r, 'about.html')
def contact(r):
    return render(r, 'contact.html')
