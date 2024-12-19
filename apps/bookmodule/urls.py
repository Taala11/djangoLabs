from django.urls import path
from . import views
urlpatterns = [
 #path('', views.index),
 #path('index2/<int:val1>/', views.index2)
 #path('<int:bookId>', views.viewbook)

 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),  # Updated name
 path('aboutus/', views.aboutus, name="books.aboutus"),
 path('html5/links/', views.links_page, name='books.links'),
 path('html5/text/formatting', views.formatting, name='formatting'),
 path('html5/listing', views.listing, name='listing'),
 path('html5/tables', views.tables, name='tables'),
 path('search', views.search, name='search'),
 path('simple/query', views.simple_query, name='simple_query'),
 path('complex/query', views.lookup_query, name='lookup_query'),
 path('lab8/task1', views.task1, name='task1'),
 path('lab8/task2', views.task2, name='task2'),
 path('lab8/task3', views.task3, name='task3'),
 path('lab8/task4', views.task4, name='task4'),
 path('lab8/task5', views.task5, name='task5'),
 path('lab8/task7', views.task7, name='task7'),
 path('lab9_part1/listbooks2', views.list_books2, name='list_books2'),
 path('lab9_part1/addbook', views.add_book, name='add_book'),
 path('lab9_part1/editbook/<int:id>', views.edit_book, name='edit_book'),
 path('lab9_part1/deletebook/<int:id>', views.delete_book, name='delete_book'),
 path('lab9_part2/listbooks2', views.list_books2_form, name='list_books2_form'),
 path('lab9_part2/addbook', views.add_book_form, name='add_book_form'),
 path('lab9_part2/editbook/<int:id>', views.edit_book_form, name='edit_book_form'),
 path('lab9_part2/deletebook/<int:id>', views.delete_book_form, name='delete_book_form'),


]
