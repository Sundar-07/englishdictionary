from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.


def index(request):
    return render(request,'dictionary/index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meanings = dictionary.meaning(search)
    synonyms = dictionary.synonym(search)
    antonyms = dictionary.antonym(search)

    context = {
        'meanings': meanings['Noun'][0:4],
        'search':search,
        'synonyms':synonyms[0:10],
        'antonyms':antonyms,
    
    }

    return render(request,'dictionary/word.html',context)
