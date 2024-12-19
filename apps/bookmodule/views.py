from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from .models import Book, Student, Address
from django.db.models import Avg, Max, Min, Sum, Count


# Create your views here.
#from django.http import HttpResponse
def index(request):
 return render(request, "bookmodule/index.html")
def list_books(request):
 return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
 return render(request, 'bookmodule/one_book.html')
def aboutus(request):
 return render(request, 'bookmodule/aboutus.html')
def links_page(request):
    return render(request, 'bookmodule/links.html')
def formatting(request):
    return render(request, 'bookmodule/formatting.html')
def listing(request):
    return render(request, 'bookmodule/listing.html')
def tables(request):
    return render(request, 'bookmodule/tables.html')
def search(request):
   if request.method == "POST":
    string = request.POST.get('keyword').lower()
    isTitle = request.POST.get('option1')
    isAuthor = request.POST.get('option2')
 # now filter
    books = __getBooksList()
    newBooks = []
    for item in books:
        contained = False
        if isTitle and string in item['title'].lower(): contained = True
        if not contained and isAuthor and string in item['author'].lower():contained = True

        if contained: newBooks.append(item)
    return render(request, 'bookmodule/bookList.html', {'books':newBooks})

def __getBooksList():
 book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
 book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
 book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
 return [book1, book2, book3]

def search_results(request):
    books = request.session.pop('filtered_books', [])  # Get and clear the session data
    return render(request, 'bookmodule/bookList.html', {'books': books})

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def lookup_query(request):
    mybooks = Book.objects.filter(author__isnull=False)\
                          .filter(title__icontains='and')\
                          .filter(edition__gte=2)\
                          .exclude(price__lte=100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
def task1(request):
    # Query for books with price <= 50
    books = Book.objects.filter(Q(price__lte=50))
    return render(request, 'bookmodule/task1.html', {'books': books})

def task2(request):
    # Query for books with editions > 2 AND (title OR author contains 'qu')
    books = Book.objects.filter(Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/task2.html', {'books': books})

def task3(request):
    # Query for books with editions <= 2 AND (title AND author does NOT contain 'qu')
    books = Book.objects.filter(
        Q(edition__lte=2) & ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/task3.html', {'books': books})

def task4(request):
    # Query for all books ordered by title
    books = Book.objects.order_by('title')
    return render(request, 'bookmodule/task4.html', {'books': books})

def task5(request):
    # Aggregate calculations for the books
    aggregate_data = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price'),
    )
    return render(request, 'bookmodule/task5.html', {'aggregate_data': aggregate_data})

def task7(request):
    # Count the number of students in each city
    student_counts = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task7.html', {'student_counts': student_counts})