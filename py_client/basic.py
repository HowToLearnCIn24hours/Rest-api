import requests
#endpoint = "https://httpbin.org/status/200"
#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"


get_response = requests.get(endpoint, json = {"query":"Hello world"}) #HTTP request
print(get_response.json()["message"]) #source code
#print(get_response.status_code) #show status code of the page