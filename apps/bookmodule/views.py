from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})

def index2(request, val1=0):
     return HttpResponse("value1 = " + str(val1))

def viewbook(request, bookId):
    if bookId == 1:
        return render(request, 'bookmodule/one_book.html')
    book1 = {
        'id': 123,
        'title': 'Continuous Delivery',
        'author': 'J. Humble and D. Farley'
    }

    book2 = {
        'id': 456,
        'title': 'Secrets of Reverse Engineering',
        'author': 'E. Eilam'
    }

    targetBook = None

    if bookId == book1['id']:
        targetBook = book1

    elif bookId == book2['id']:
        targetBook = book2

    return render(
        request,
        'bookmodule/show.html',
        {'book': targetBook}
    )

def list_books(request):
    return render(request, 'bookmodule/list_books.html')



def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')


def links(request):
    return render(request, 'books/links.html')


def text_formatting(request):
    return render(request, 'books/text_formatting.html')


def listing(request):
    return render(request, 'books/listing.html')


def tables(request):
    return render(request, 'books/tables.html')

def search(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword', '').strip().lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []

        for book in books:
            contained = False

            if isTitle and keyword in book['title'].lower():
                contained = True

            if isAuthor and keyword in book['author'].lower():
                contained = True

            if contained:
                newBooks.append(book)

        return render(
            request,
            'bookmodule/bookList.html',
            {'books': newBooks}
        )

    return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {
        'id': 12344321,
        'title': 'Continuous Delivery',
        'author': 'J. Humble and D. Farley'
    }

    book2 = {
        'id': 56788765,
        'title': 'Reversing: Secrets of Reverse Engineering',
        'author': 'E. Eilam'
    }

    book3 = {
        'id': 43211234,
        'title': 'The Hundred-Page Machine Learning Book',
        'author': 'Andriy Burkov'
    }

    return [book1, book2, book3]