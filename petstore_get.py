import requests

status = 'available'
#GET
res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept':'application/json'})

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

#POST
url = 'https://petstore.swagger.io/v2/pet'
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res1 = requests.post(url, json=data, headers=headers)
print(res1.status_code)
print(res1.json())

#PUT


res2 = requests.put(url, headers=headers, json=data)
print(res2.status_code)
print(res2.json())

#DELETE


res3 = requests.delete(f'https://petstore.swagger.io/v2/pet/9223372036854755854', headers={'accept': 'application/json'})
print(res3.status_code)
print(res3.json())

