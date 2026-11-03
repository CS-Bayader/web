from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.db.models import Q, Count, Sum, Avg, Max, Min
from apps.usermodule.models import Address

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
def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')

    return render(
        request,
        'bookmodule/bookList.html',
        {'books': mybooks}
    )
def complex_query(request):
    mybooks = (
        Book.objects
        .filter(author__isnull=False)
        .filter(title__icontains='and')
        .filter(edition__gte=2)
        .exclude(price__lte=100)
    )[:10]

    if mybooks:
        return render(
            request,
            'bookmodule/bookList.html',
            {'books': mybooks}
        )

    return render(
        request,
        'bookmodule/index.html',
        {'name': 'world!'}
    )
def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))

    return render(
        request,
        'bookmodule/bookList.html',
        {'books': books}
    )
def lab8_task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) &
        (Q(title__icontains='co') | Q(author__icontains='co'))
    )

    return render(
        request,
        'bookmodule/bookList.html',
        {'books': books}
    )
def lab8_task3(request):
    books = Book.objects.filter(
        ~(
            Q(edition__gt=3) &
            (Q(title__icontains='co') | Q(author__icontains='co'))
        )
    )

    return render(
        request,
        'bookmodule/bookList.html',
        {'books': books}
    )
def lab8_task4(request):
    books = Book.objects.order_by('title')

    return render(
        request,
        'bookmodule/bookList.html',
        {'books': books}
    )

def lab8_task5(request):
    stats = Book.objects.aggregate(
        book_count=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price'),
    )

    return render(request, 'bookmodule/lab8_task5.html', {'stats': stats})
def lab8_task7(request):
    cities = (
        Address.objects
        .values('city')
        .annotate(student_count=Count('student'))
        .order_by('city')
    )

    return render(
        request,
        'bookmodule/lab8_task7.html',
        {'cities': cities}
    )
