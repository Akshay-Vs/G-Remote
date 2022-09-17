from sys import argv
import requests
import json
import color

#argv path_to_readme user repo

response = requests.request("GET",f"https://api.github.com/repos/{argv[2]}/{argv[3]}")
response = json.loads(response.text)

user = response["owner"]["login"]
repo = response["name"]
description = response["description"]
avatar = response["owner"]["avatar_url"]

#languages
language = response["languages_url"]
language = requests.request("GET", language)
language = json.loads(language.text)

with open(argv[1], 'r') as file:
    Readme = file.read()
    Readme = Readme.replace('{User}',user)
    Readme = Readme.replace('{Repo}',repo)
    Readme = Readme.replace('{Description}',description)
    Readme = Readme.replace('{Avatar}',avatar)

    if response["license"] != None:
        license = response["license"]["name"]
        Readme = Readme.replace('{License}',license)

    if len(language)>1:
        primary_language = list(language)[0]
        secondary_language = list(language)[1]
        Readme = Readme.replace('{Primary Language}',primary_language)
        Readme = Readme.replace('{Version}','0.0')
        Readme = Readme.replace('{Secondary language}',secondary_language)
    result = open("result.md",'w+').write(Readme)

    

