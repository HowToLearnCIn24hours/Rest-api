import requests
import json
#endpoint = "https://httpbin.org/status/200"
#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"


get_response = requests.get(endpoint, params = {"abc": 123}, json = {"query":"Hello world"}) #HTTP request
print(get_response.json()) #source code
#print(get_response.status_code) #show status code of the page