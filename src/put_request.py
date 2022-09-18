import requests
import json
from sys import argv
from base64enc import encode
from color import Colors

data = encode(open(argv[1], 'r').read())
auth = argv[2]
username = argv[3]
Repo = argv[4]
filename = argv[5]

url = f"https://api.github.com/repos/{username}/{Repo}/contents/{filename}"

payload = json.dumps({
  "message": f"Create {argv[5]}",
  "content": f"{data}"
})
headers = {
  'Authorization': f'Bearer {auth}',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

if response.status_code==201:Colors.Print(f"201: Successfully Created {filename}")
else:Colors.Print(f"{response.status_code}: Failed to push {argv[1]}", "LIGHT_RED")
