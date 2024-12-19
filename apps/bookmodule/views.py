from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from .models import Book, Student, Address, Gallery
from django.db.models import Avg, Max, Min, Sum, Count
from apps.bookmodule.forms import BookForm, StudentForm, GalleryForm


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

def list_books2(request):
    # Fetch all books from the database
    books = Book.objects.all()
    return render(request, 'bookmodule/list_books2.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        # Get data from the form
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        
        # Create and save a new book
        Book.objects.create(title=title, author=author, price=price)
        
        # Redirect to the book list
        return redirect('list_books')
    
    # Render the add book form
    return render(request, 'bookmodule/add_book.html')


def edit_book(request, id):
    # Fetch the book to be edited
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        # Update the book with form data
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.save()  # Save changes to the database
        
        # Redirect to the book list
        return redirect('list_books')
    
    # Render the edit form with existing book data
    return render(request, 'bookmodule/edit_book.html', {'book': book})

def delete_book(request, id):
    # Fetch the book to be deleted
    book = get_object_or_404(Book, id=id)
    
    # Delete the book
    book.delete()
    
    # Redirect to the book list
    return redirect('bookmodule/list_books2')

def list_books2_form(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/list_books2_form.html', {'books': books})

def add_book_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books2_form')
    else:
        form = BookForm()
    return render(request, 'bookmodule/add_book_form.html', {'form': form})

def edit_book_form(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books2_form')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/edit_book_form.html', {'form': form})

def delete_book_form(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books2_form')
    return render(request, 'bookmodule/delete_book_form.html', {'book': book})

def list_students(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/list_students.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            form.save_m2m()  # Save many-to-many relationships
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'bookmodule/add_student.html', {'form': form})

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            form.save_m2m()  # Save many-to-many relationships
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'bookmodule/edit_student.html', {'form': form})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students')
    return render(request, 'bookmodule/delete_student.html', {'student': student})

def list_gallery(request):
    images = Gallery.objects.all()
    return render(request, 'bookmodule/list_gallery.html', {'images': images})

def add_gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)  # Include FILES for image upload
        if form.is_valid():
            form.save()
            return redirect('list_gallery')
    else:
        form = GalleryForm()
    return render(request, 'bookmodule/add_gallery.html', {'form': form})

def delete_gallery(request, id):
    image = get_object_or_404(Gallery, id=id)
    if request.method == 'POST':
        image.delete()
        return redirect('list_gallery')
    return render(request, 'bookmodule/delete_gallery.html', {'image': image})


