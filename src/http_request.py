import sys
import requests
import json
from color import Colors

url = "https://api.github.com/user/repos"

print(sys.argv)

payload = json.dumps({
  "name": f"{sys.argv[2]}",
  "description": f"{sys.argv[3]}",
   "private":  f"{sys.argv[4]}",
})
headers = {
  'Authorization': f'Bearer {sys.argv[1]}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

if response.status_code==201:Colors.Print(f"Successfully created {sys.argv[2]}")
else: Colors.Print(f"Failed to create {sys.argv[2]}","LIGHT_RED")
