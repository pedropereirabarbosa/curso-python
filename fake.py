#FakeStore -> produtos
import requests as req

response = req.get('https://fakestoreapi.com/products/2')

data = response.json()

print(data['title'])
print(data['price'])
