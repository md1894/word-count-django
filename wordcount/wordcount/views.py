
from django.http import HttpResponse
from django.shortcuts import render
import operator 

def homepage(request):
    return render(request,'word-count-home.html')


def home(request):
    return HttpResponse('hello')

def demohtml(request):
    return HttpResponse('<h1>hello<h1>')

def demoTemplate(request):
    return render(request,'home.html',{'key':'this value is passed in html page'})

def countwords(request):
    fulltext = request.GET['fulltext']
    #print(fulltext)
    wordlist = fulltext.split()
    
    wordCountDict = {}

    for word in wordlist:
        if word in wordCountDict:
            #increase 
            wordCountDict[word] += 1
        else:
            #add to dict
            wordCountDict[word] = 1

        sortedwords = sorted(wordCountDict.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'word_dict':sortedwords})