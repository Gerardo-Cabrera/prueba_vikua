from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Book
from libros.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        # form = UserCreationForm()
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class BookList(ListView):
    model = Book


class BookDetail(DetailView):
    model = Book


class BookCreation(CreateView):
    model = Book
    success_url = reverse_lazy('courses:list')
    fields = ['name', 'author', 'publication_date']


class BookUpdate(UpdateView):
    model = Book
    success_url = reverse_lazy('courses:list')
    fields = ['name', 'author', 'publication_date']


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('courses:list')