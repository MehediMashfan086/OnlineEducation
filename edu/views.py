from django.http.request import host_validation_re
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib import messages
from django.views import generic

# Create your views here.
def home(request):
    return render(request, 'edu/home.html')

def notes(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user, title=request.POST['title'],
                          description=request.POST['description'])
            notes.save()
        messages.success(request, f"Notes Added from {request.user.username} Sucessfully !!")
    else:
        form = NotesForm()
    notes = Notes.objects.filter(user = request.user)
    context = {'notes': notes, 'form': form}
    return render(request, 'edu/notes.html', context)

def delete_note(request, pk = None):
    Notes.objects.get(id = pk).delete()
    return redirect('notes')

class NotesDetailView(generic.DetailView):
    model = Notes

def homework(request):
    if request.method == "POST":
        form = HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True 
                else:
                    finished = False
            except:
                finished = False
            homeworks = Homework(user=request.user, 
                          subject = request.POST['subject'],
                          title = request.POST['title'],
                          description = request.POST['description'],
                          due = request.POST['due'],
                          is_finished = finished
                        )
            homeworks.save()
        messages.success(request, f"Homework Added from {request.user.username} Sucessfully !!")
    else:
        form = HomeworkForm()
    homework = Homework.objects.filter(user = request.user)
    if len(homework) == 0:
        homework_done = True
    else:
        homework_done = False
    context = {'homeworks': homework, 'homeworks_done': homework_done, 'form': form}
    return render(request, 'edu/homework.html', context)

def update_homework(request, pk=None):
    homework = Homework.objects.get(id=pk)
    if homework.is_finished == True:
        homework.is_finished = False
    else:
        homework.is_finished = True
    homework.save()
    return redirect('homework')
        
def delete_homework(request, pk = None):
    Homework.objects.get(id = pk).delete()
    return redirect('homework')

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
