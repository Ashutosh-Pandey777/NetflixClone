# I have create this file - Ashu
from django.http import HttpResponse
from django.shortcuts import render

# code for vedio 6
# def index(request):
# return HttpResponse('''<h1>Ashu</h1>  <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django code with harry</a>''')

# def about(request):
#     return HttpResponse("About Ashu Bhai")

# code for video 7
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")

# code for Excersize
def Excersize(request):
    return HttpResponse('''<h1>Navigation Bar</h1><br>
            <a href="https://www.codewithharry.com/">Code with Harry</a><br>
            <a href="https://www.facebook.com/">Facebook</a><br>
            <a href="https://www.google.com/search?q=google&rlz=1C1ONGR_enIN974IN974&oq=google&aqs=chrome..69i57j69i59l3j69i60l3j69i65.3921j0j4&sourceid=chrome&ie=UTF-8"> Google</a><br>
            <a href="https://www.instagram.com/poonamdubeyofficial/?hl=en">Instagram</a>''')


# def removepunc(request):
#     # Get the text
#     djtext = request.GET.get('text', 'default')
#     # Analyze the text
#     print(djtext)
#     return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("new line remove")
#
# def spaceremove(request):
#     return HttpResponse("space remove")
#
# def charcount(request):
#     return HttpResponse("char count")


# video 11
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
        # return render(request, 'analyze.html', params)


    if(fullcaps=='on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyzed the text
        # return render(request, 'analyze.html', params)

    if(newlineremove=='on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params ={'purpose': 'Remove New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyzed the text
        # return render(request, 'analyze.html', params)

    if(extraspaceremover=='on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Extra space Remover', 'analyzed_text': analyzed}
        # djtext = analyzed
        # Analyzed the text
        # return render(request, 'analyze.html', params)

    # if(charcount=='on'):
    #     analyzed = ""
    #     for char in djtext:
    #             analyzed = analyzed + char
    #
    #     params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
    #     # Analyzed the text
        # return render(request, 'analyze.html', params)

    if(removepunc!= "on" and newlineremove!= "on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("Please select the any operstion and try again")


    return render(request, 'analyze.html', params)