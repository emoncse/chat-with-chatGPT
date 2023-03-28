import requests
from django.http import JsonResponse
from django.shortcuts import render


def process_text(text):
    return text.replace('\\n', '\n ')


def chat_page(request):
    return render(request, 'chat.html')


def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = requests.post('https://api.openai.com/v1/engines/curie/completions', json={
            "prompt": message,
            "max_tokens": 100,
            "temperature": 0.5
        }, headers={
            'Authorization': 'Bearer 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'
        })
        print(response.content)
        if response.ok:
            print(response.content)
            response_text = response.json()['choices'][0]['text']
            response_text = process_text(message + response_text)
        else:
            response_text = "Oops, something went wrong"
        print(response_text)
        return JsonResponse({'response_text': response_text})