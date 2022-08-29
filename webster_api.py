import requests

API_KEY = '90ab9366-dd6d-45e9-8aca-b55b9e6a3e26'

def is_word(word):
    link = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={API_KEY}'
    response = requests.get(link)
    json_dict = response.json()

    return len(json_dict) > 0 and type(json_dict[0]) == dict