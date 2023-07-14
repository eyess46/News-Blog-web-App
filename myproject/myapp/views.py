from django.shortcuts import render, redirect
from .models import News, Sport, Politics, Business
from .models import Contactform


def index(request):

    news = News.objects.all()
    sport = Sport.objects.all()
    politics = Politics.objects.all()
    business = Business.objects.all()

    return render(request, 'index.html', {'news': news, 'sport': sport, 'politics': politics, 'business': business})


def news(request, pk):    
    news = News.objects.get(id=pk)
    
    return render(request, 'news.html', {'news': news})

def sport(request, pk):    
    sport = Sport.objects.get(id=pk)
    
    return render(request, 'sport.html', {'sport': sport}) 

def business(request, pk):    
    business = Business.objects.get(id=pk)
    
    return render(request, 'business.html', {'business': business})    

def politics(request, pk):    
    politics = Politics.objects.get(id=pk)
    
    return render(request, 'politics.html', {'politics': politics})    


def contact(request):
   
   if request.method == "POST":                    
        name = request.POST.get('name')      
        email = request.POST.get('email')        
        subject = request.POST.get('subject') 
        message = request.POST.get('message')            
                       
        print(name, email, subject, message)            
        Contactform.objects.create(name=name, email=email, subject=subject, message=message,)       
        return redirect('index')  

   else:
      return render(request, 'contact.html', )           