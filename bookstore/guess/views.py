from django.shortcuts import render
from guess.models import Guess
# Create your views here.    

def guess(request): 
    answer = Guess.answer
    guessNum = request.GET.get('guessNum')
   
    solution = "" 
    if not guessNum:
        solution = ""   
    else:
        guessNum = int(guessNum)
        if guessNum==answer: 
            solution='答對了'
        elif guessNum>answer: 
            solution='太大了'
        elif guessNum<answer: 
            solution='太小了'
    context = {'solution':solution} 
    return render(request, 'guess/guess.html', context)


