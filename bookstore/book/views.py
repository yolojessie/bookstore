from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models.query_utils import Q
from django.contrib.auth.decorators import login_required
from main.views import admin_required
from book.models import Book
from book.forms import BookForm
import book
# Create your views here.
def book(request):
    '''
    Render the book page
    '''
    bkNames = Book.objects.all()
    context = {'bkNames':bkNames}
    
    return render(request, 'book/book.html',context)

@admin_required
def bookCreate(request):
    '''
    Create a new article instance
        1. If method is GET, render an empty form
        2. If method is POST, perform form validation and display error messages if the form is invalid
        3. Save the form to the model and redirect the user to the article page
    '''
    template = 'book/bookCreateUpdate.html'
    if request.method == 'GET':
        return render(request, template, {'bookForm':BookForm()})
    
    # POST
    bookForm = BookForm(request.POST)
    if not bookForm.is_valid():
        return render(request, template, {'bookForm':bookForm})
    bookForm.save()
    messages.success(request, '文章已新增')
    return redirect('book:book')

@login_required
def bookRead(request, bookId):
    book = get_object_or_404(Book, id=bookId)
    context = {
        'book': book
    }
    return render(request, 'book/bookRead.html', context)

@admin_required
def bookUpdate(request, bookId):
    book = get_object_or_404(Book, id=bookId)
    template = 'book/bookCreateUpdate.html'
    if request.method == 'GET':
        bookForm = BookForm(instance=book)
        return render(request, template, {'bookForm':bookForm})

    # POST
    bookForm = BookForm(request.POST, instance=book)
    if not bookForm.is_valid():
        return render(request, template, {'bookForm':bookForm})
    bookForm.save()
    messages.success(request, '文章已修改') 
    return redirect('book:bookRead', bookId=bookId)

@admin_required
def bookDelete(request, bookId):
    '''
    Delete the article instance:
        1. Render the article page if the method is GET
        2. Get the article to delete; redirect to 404 if not found
    '''
    if request.method == 'GET':
        return book(request)
    # POST
    book = get_object_or_404(Book, id=bookId)
    book.delete()
    messages.success(request, '文章已刪除')  
    return redirect('book:book')

def bookSearch(request):
    '''
    Search for articles:
        1. Get the "searchTerm" from the HTML page
        2. Use "searchTerm" for filtering
    '''
    searchTerm = request.GET.get('searchTerm')
    minPrice = request.GET.get('minPrice')
    books = Book.objects.filter((Q(bkName__icontains=searchTerm) |
                                      Q(authorName__icontains=searchTerm))&
                                      Q(price__gte=minPrice))
    print(type(minPrice))
    context = {'books':books, 'searchTerm':searchTerm, 'minPrice':minPrice} 
    return render(request, 'book/bookSearch.html', context)

@login_required
def booksold(request, bookId):
    '''
    Add the user to the 'likes' field:
        1. Get the article; redirect to 404 if not found
        2. If the user does not exist in the "likes" field, add him/her
        3. Finally, call articleRead() function to render the article
    '''
    book = get_object_or_404(Book, id=bookId)
    if request.user not in book.sold.all():
        book.sold.add(request.user)
        book.inventory = book.inventory-1
        book.save()
    else:
        book.sold.remove(request.user)
        book.inventory = book.inventory+1
        book.save()
    return bookRead(request, bookId)
