# I have create this file - Ashu
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')


    # Check Checkbox Values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # checks which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                 analyzed = analyzed + char

        params ={'purpose':'Removed punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps=='on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed


    if(newlineremove=='on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params ={'purpose': 'Remove New Lines', 'analyzed_text': analyzed}
        djtext = analyzed


    if(extraspaceremover=='on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Extra space Remover', 'analyzed_text': analyzed}

    if(removepunc!= "on" and newlineremove!= "on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("Please select the any operstion and try again")


    return render(request, 'analyze.html', params)