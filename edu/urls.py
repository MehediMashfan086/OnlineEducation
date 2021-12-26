from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.notes, name='notes'),
    path('delete_note/<int:pk>', views.delete_note, name='delete_note'),
    path('notes_detail/<int:pk>', views.NotesDetailView.as_view(), name='notes_detail'),
    path('homework/', views.homework, name='homework'),
    path('youtube/', views.youtube, name='youtube'),
    path('todo/', views.todo, name='todo'),
    path('books/', views.books, name='books'),
    path('dictionary/', views.dictionary, name='dictionary'),
    path('wiki/', views.wiki, name='wiki'),
    path('conversion/', views.conversion, name='conversion'),
]