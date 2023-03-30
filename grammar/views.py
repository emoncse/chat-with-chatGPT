import os
from dotenv import load_dotenv
import requests
from django.http import JsonResponse
from django.shortcuts import render
import openai


def process_text(text):
    return text.replace('\\n', '\n ')


def grammar_page(request):
    return render(request, 'sentence.html')


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


def check(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')

        merge_text = "Convert the below sentence to " + str(option1) + " " + str(option2) + ": \n " + str(message)
        print("Merge Text " + merge_text)
        response = getting_ready(merge_text)
        print(response)

        if response:
            # print(response)
            response_text = response
        else:
            response_text = "Oops, something went wrong"
        return JsonResponse({'response_text': response_text})
