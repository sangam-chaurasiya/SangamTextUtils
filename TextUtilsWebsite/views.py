# I have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    text = request.POST.get('mytext', 'It is a default text')
    params = {'purpose': '', 'analyzed_text': ''}

    # Check Checkbox Value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')


    # Check which checkbox is on
    if removepunc == 'on' or fullcaps == 'on' or newlineremove == 'on' or spaceremove == 'on' or charcount == 'on':

        if removepunc == 'on':
            punctuations = '''!@#$%^&*()_-{}[]<>?/\,.;:'"`~'''
            analyzed = ""
            for ch in text:
                if ch not in punctuations:
                    analyzed += ch
            params = {'purpose': 'Remove Punctuations, ', 'analyzed_text': analyzed}
            text = analyzed

        if fullcaps == 'on':
            analyzed = ""
            for char in text:
                analyzed += char.upper()
            params = {'purpose': params['purpose'] + 'Fully Capitalized, ', 'analyzed_text': analyzed}
            text = analyzed

        if newlineremove == 'on':
            analyzed = ""
            for char in text:
                if char != "\n":
                    analyzed = analyzed + char
            params = {'purpose': params['purpose'] + 'Removed NewLines', 'analyzed_text': analyzed}
            text = analyzed

        if spaceremove == 'on':
            analyzed = ""

            for ind, char in enumerate(text[:-1] if text[-1] == " " else text):
                if not(text[ind] == " " and text[ind + 1] == " "):
                    analyzed += char
            params = {'purpose': params['purpose'] + 'Space Remover, ', 'analyzed_text': analyzed}
            text = analyzed

        if charcount == 'on':
            analyzed = '"' + text + '"' + " has " + str(len(text)) + " characters"
            params = {'purpose': params['purpose'] + 'Character Counter', 'analyzed_text': analyzed}

        # analyze the text
        return render(request, 'analyze.html', params)

    return HttpResponse("<h1 style='color:red'>Error!</h1>")
