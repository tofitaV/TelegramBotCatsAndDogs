import requests


def API(api, url):
    headers = {'x-api-key': api}

    response = requests.get(url, headers=headers)

    json_response = response.json()
    return json_response[0]['url']


def CatsAPI():
    API_KEY = 'e86ef7c4-b448-4083-9fd9-768286f3fb34'
    URLToCats = 'https://api.thecatapi.com/v1/images/search'
    return API(API_KEY, URLToCats)


def DogsAPI():
    API_KEY = '2907b483-646a-4db5-850e-5adb2d204c5a'
    URLToCats = 'https://api.thedogapi.com/v1/images/search'
    return API(API_KEY, URLToCats)
