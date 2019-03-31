from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,'homepage.html')

def count(request):
    data=request.GET['fulltextarea']
    word_list=data.split()
    word_len=len(word_list)
    return render(request,'count.html',{'fulltext':data,'wcount':word_len})
