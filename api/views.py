import string

from django.http import HttpResponse, JsonResponse
from grammar import views
import os
from dotenv import load_dotenv
import openai


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


def grammar(request):
    if request.method == 'GET':
        tense = request.GET.get('tense')
        types = request.GET.get('types')
        data = request.GET.get('data')

        if not tense or not types or not data:
            return JsonResponse({
                'request_code': 400,
                'text': 'Missing parameters'
            })

        st = "Convert the below sentence to "
        combined_text = st + str(tense) + " " + str(types) + ": \n " + str(data)
        print("Merge Text " + combined_text)
        response = getting_ready(combined_text)
        print(response)
        if response:
            response_text = response
        else:
            response_text = "Oops, something went wrong"
        data = {
            'request_code': 200,
            'text': 'Success',
            'result': response_text,
        }
        return JsonResponse(data)
    data = {
        'request_code': 200,
        'text': 'failed',
    }
    return JsonResponse(data)
