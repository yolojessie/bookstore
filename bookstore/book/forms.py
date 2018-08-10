from django import forms
from book.models import Book
from cProfile import label


class BookForm(forms.ModelForm):
    bkName = forms.CharField(label='書名',max_length=128)
    authorName = forms.CharField(label='作者',max_length=128)
    publisher = forms.CharField(label='出版商',max_length=128)
    pubversion = forms.IntegerField(label='版次')
    price = forms.IntegerField(label='價格')   
    inventory = forms.IntegerField(label='庫存') 

    class Meta:
        model = Book
        fields = ['bkName', 'authorName','publisher','pubversion','price','inventory']
        