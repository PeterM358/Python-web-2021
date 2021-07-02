from django.shortcuts import render, redirect, get_object_or_404

from books_app.books.forms import BookForm
from books_app.books.models import Book


def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'index.html', context)


def create_book(request):
    if request.method == 'GET':
        context = {
            'form': BookForm()
        }
        return render(request, 'create.html', context)
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'index.html', form)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': BookForm(
                initial=book.__dict__,  # gives all created book data
            )
        }
        return render(request, 'edit.html', context)
    else:
        form = BookForm(
            request.POST,
            instance=book,
        )
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'edit.html', form)
    # watch model forms 1:40:00 to reduce code


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('index')

    context = {
        'form': BookForm(
            initial=book.__dict__
        )
    }
    return render(request, 'delete.html', context)
