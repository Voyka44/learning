import requests
response = requests.post('https://httpbin.org/post', json={'key':'value'})
json_response = response.json()
json_response['data']
'{"key": "value"}'
json_response['headers']['Content-Type']
'application/json'
print(json_response)