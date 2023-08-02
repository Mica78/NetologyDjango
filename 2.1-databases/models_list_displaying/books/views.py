from django.shortcuts import render, redirect
from django.db.models import Max, Min
from books.models import Book
from books.converters import DateConverter


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return redirect('books/')
    # return render(request, template, context)


def books_view_new(request):
    template = 'books/books_list_new.html'
    context = {
        'books': Book.objects.all()
    }
    return render(request, template, context)


def book_view_at_date(request, pub_date: str):
    converter = DateConverter()
    converted_date_to_python = converter.to_python(pub_date)

    try:
        prev_date_obj = Book.objects.filter(pub_date__lt=converted_date_to_python).aggregate(Max('pub_date')).values()
        prev_date = converter.to_url(*prev_date_obj)
    except AttributeError:
        prev_date = None

    try:
        next_date_obj = Book.objects.filter(pub_date__gt=converted_date_to_python).aggregate(Min('pub_date')).values()
        next_date = converter.to_url(*next_date_obj)
    except AttributeError:
        next_date = None

    template = 'books/books_list_new.html'
    context = {
        'books': Book.objects.filter(pub_date=converted_date_to_python),
        'prev_date': prev_date,
        'next_date': next_date
    }
    return render(request, template, context)
