from populate import base
from account.models import User
from book.models import Book
from book.views import book


bkNames = ['如何像電腦科學家一樣思考', '10分鐘內學好Python', '簡單學習Django', '學Django', 'Django'
          , '學習Django', '簡單Django', '簡單學', '簡單學習Python', '簡單學Django']


def populate():
    print('Populating bkName ... ', end='')
    Book.objects.all().delete()
    i=1
    for bkName in bkNames:
        book = Book()
        book.bkName = bkName
        book.authorName = 'at'+str(i)
        book.publisher = 'pub'+str(i)
        book.pubversion = 1
        book.price = i*100
        book.inventory = 10
        i+=1
        book.save()
        
    print('done')


if __name__ == '__main__':
    populate()