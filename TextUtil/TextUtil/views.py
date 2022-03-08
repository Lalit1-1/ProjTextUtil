# I have created this file - 'Lalit'

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # GEt The Text
    djtext = request.POST.get('text', 'default')

    # Check  checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # Check which checkbox is on
    if(removepunc == "on"):
        punctuations = '''!()-[]{};:"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char

        params = {'purpose' : 'Removed Punctuations', 'analyzed_text' : analyzed}
        djtext = analyzed

    # Analyze the Text
    if(fullcaps=="on"): # (All btn se kam krna hey) Yha tak aa ke fiir se chk kro ke full-caps on hey ke nhe
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to UpperCase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]== ""):
                analyzed = analyzed + char

        params = {'purpose': 'Removed ExtraSpace', 'analyzed_text': analyzed}

    if(removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("Please select any operation and try again")

    # Analyze the Text
    return render(request, 'analyze.html', params)