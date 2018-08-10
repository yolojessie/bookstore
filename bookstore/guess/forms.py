from django import forms
from book.models import Book
from cProfile import label


class GuessForm(forms.Form):
    guessNum = forms.IntegerField(label='請猜一個 0~9 的數字:')
    

        