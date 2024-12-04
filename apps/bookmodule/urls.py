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

]
