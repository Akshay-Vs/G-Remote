from sys import argv
from base64enc import encode
from os import system
from color import Colors
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

    if response["license"] != None:
        license = response["license"]["name"]
        Readme = Readme.replace('{License}',license)

    if len(language)>1:
        primary_language = list(language)[0]
        secondary_language = list(language)[1]
        Readme = Readme.replace('{Primary Language}',primary_language)
        Readme = Readme.replace('{Version}','0.0')
        Readme = Readme.replace('{Secondary language}',secondary_language)
    result = open("Readme.md",'w+').write(Readme)

Colors.Print("[Info] Readme.md Generated from Black-Night template")

#put data
# data = encode(open(argv[4], 'r').read())
# url = f"https://api.github.com/repos/{argv[2]}/{argv[3]}/contents/Readme.md"

# put_header= {
#   'Authorization': f'Bearer {argv[1]}',
#   'Content-Type': 'application/json'
# }

# payload = json.dumps({
#   "message": "Create Readme.md",
#   "content": f"{data}"
# })
# response = requests.request("PUT", url, headers=put_header, data=payload)
# print(response.text)
# if response.status_code==201:Colors.Print(f"201: Successfully Created Readme.md")
# else:Colors.Print(f"{response.status_code}: Failed to push Readme.md", "LIGHT_RED")
