import requests

# url = 'http://localhost:8000/test'
url = 'https://rcw-test-g8efatdnbsc4d7a6.canadaeast-01.azurewebsites.net/test'

response = requests.get(url)
response = response.json()
print(response['message'])