from django.urls import path
from book import views


app_name = 'book'
urlpatterns = [
    path('', views.book, name='book'),
    path('bookCreate/', views.bookCreate, name='bookCreate'),
    path('bookRead/<int:bookId>/', views.bookRead, name='bookRead'),
    path('bookUpdate/<int:bookId>/', views.bookUpdate, name='bookUpdate'),
    path('bookDelete/<int:bookId>/', views.bookDelete, name='bookDelete'),
    path('bookSearch/', views.bookSearch, name='bookSearch'),
    path('booksold/<int:bookId>/', views.booksold, name='booksold'),
]
