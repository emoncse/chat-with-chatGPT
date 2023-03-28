import os

from dotenv import load_dotenv
import requests
from django.http import JsonResponse
from django.shortcuts import render
import openai


def process_text(text):
    return text.replace('\\n', '\n ')


def chat_page(request):
    return render(request, 'chat.html')


def getting_ready(message):
    load_dotenv()
    openai.api_key = os.getenv('API_KEY')
    openai.organization = os.getenv('ORG_KEY')

    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return str(completion.choices[0].text)


def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = getting_ready(message)
        # print(response)
        if response:
            # print(response)
            response_text = response
        else:
            response_text = "Oops, something went wrong"
        # print(response_text)
        return JsonResponse({'response_text': response_text})