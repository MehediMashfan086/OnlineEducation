from django.shortcuts import render

from edu.models import Notes

# Create your views here.
def home(request):
    return render(request, 'edu/home.html')

def notes(request):
    notes = Notes.objects.all()
    context = {'notes': notes}
    return render(request, 'edu/notes.html', context)

def homework(request):
    return render(request, 'edu/homework.html')

def youtube(request):
    return render(request, 'edu/youtube.html')

def todo(request):
    return render(request, 'edu/todo.html')

def books(request):
    return render(request, 'edu/books.html')

def dictionary(request):
    return render(request, 'edu/dictionary.html')

def wiki(request):
    return render(request, 'edu/wiki.html')

def conversion(request):
    return render(request, 'edu/conversion.html')
