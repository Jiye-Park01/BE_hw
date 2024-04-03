from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def wordCount(request):
    return render(request, "wordCount.html")
def result(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()

    word_dictionary = {}
    
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    return render(request, "result.html", {'alltext': entered_text, 'dictionary': word_dictionary.items(), 'count':len(word_list), 'word_num':len(entered_text), 'word_except':len(entered_text)-len(word_list)+1})

def hello(request):
    entered_name = request.GET['getName']  
    return render(request, "hello.html", {'name_text': entered_name})