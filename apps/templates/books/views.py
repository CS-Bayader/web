from django.shortcuts import render


def links(request):
    return render(request, 'books/links.html')


def text_formatting(request):
    return render(request, 'books/text_formatting.html')


def listing(request):
    return render(request, 'books/listing.html')


def tables(request):
    return render(request, 'books/tables.html')