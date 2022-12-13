from django.shortcuts import render
import requests
import json


def home(request):
    news_api_request = requests.get(
        "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=2529141a9c0e4a158ef5d25b0da17ef2"
    )
    api=json.loads(news_api_request.content)
    return render(request, 'home.html', {'api':api})


