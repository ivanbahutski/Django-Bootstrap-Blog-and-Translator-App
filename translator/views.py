from django.shortcuts import render
from . import translate


def translator_view(request):
    if request.method == 'POST':
        orig_text = request.POST['my_textarea']
        output = translate.translator(orig_text)
        context = {
            'orig_text': orig_text,
            'output': output
        }
        return render(request, 'translator.html', context)
    else:
        return render(request, 'translator.html')
