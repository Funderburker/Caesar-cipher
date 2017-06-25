from django.shortcuts import render
from django.template import Context, loader
from somepain.models import InitialText
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from .forms import Encrypt
from nltk.corpus import wordnet


def index(request):
    if request.method == "POST":
        form = Encrypt(request.POST)
        if form.is_valid():
            req_txt = form.cleaned_data
            text = req_txt["init"].lower()
            words = text.split(' ')  # разбить текст на отдельные слова
            if DictCheck(words) > 0:  #если введенный текст - шифр
                offset = DictCheck(words)
                word = Enc(text, offset)
            else:
                word = ""
                offset = 0
            EncText = Enc(text, req_txt["ofs"])
            context = {
                'form': form,
                'txt': text,
                'enctext': EncText,
                'word' : word,
                'ofc' : offset
            }
            return render(request, "InitialText/index.html", context)
    else:
        form = Encrypt()
    return render(request, "InitialText/index.html", {'form':form})


# функция, смещающая текст на заданное значение
def Enc(text, offset):
    EncText = ""
    for i in range(len(text)):
        if 96 < ord(text[i]) < 123:
            newchar = ord(text[i]) + int(offset)
            if newchar < 123:
                EncText = EncText + chr(newchar)
            else:
                EncText = EncText + chr(96 + (newchar - 122))
        else:
            EncText = EncText + text[i]
    return EncText


# проверка на то, является ли введенный текст шифром
# проверка осуществляется по первому слову
def DictCheck(words):
      EncText = ""
      for i in range(len(words[0])):
          for j in range(27):
              if wordnet.synsets(Enc(words[0], j)):  # сместить текст на j позиций и проверить наличие слова в словаре
                  return j
      return 0