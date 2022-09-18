from sys import argv
from base64enc import encode
from os import system
from color import Colors
from datetime import date
import requests
import json

#argv auth user repo path_to_readme
Colors.Print("[Info] Generating Readme")
Colors.Print("[Info] Downloading Template")

headers = {
    'Authorization': f'Bearer {argv[1]}'
}

response = requests.request("GET", f"https://api.github.com/repos/{argv[2]}/{argv[3]}", headers=headers)
response = json.loads(response.text)

#print(response)
Colors.Print("[Info] Writing Contents")

user = response["owner"]["login"]
repo = response["name"]
description = response["description"]
avatar = response["owner"]["avatar_url"]

#languages
language = response["languages_url"]
language = requests.request("GET", language)
language = json.loads(language.text)

with open(argv[4], 'r') as file:
    Readme = file.read()
    Readme = Readme.replace('{User}',user)
    Readme = Readme.replace('{Repo}',repo)
    Readme = Readme.replace('{Description}',description)
    Readme = Readme.replace('{Avatar}',avatar)
    Readme = Readme.replace('{Year}', f"{date.today().year}")

    if response["license"] != None:
        license = response["license"]["name"]
        Readme = Readme.replace('{License}',license)

    if len(language)>1:
        primary_language = list(language)[0]
        secondary_language = list(language)[1]
        Readme = Readme.replace('{Primary Language}',primary_language)
        Readme = Readme.replace('{Version}','0.0')
        Readme = Readme.replace('{Secondary language}',secondary_language)
    result = open("Readme_.md",'w+').write(Readme)

Colors.Print("[Info] Generated Readme.md from Black-Night template")