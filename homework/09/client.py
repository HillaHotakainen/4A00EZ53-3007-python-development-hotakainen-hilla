
import requests

url = 'http://127.0.0.1:5000/posts'
myobj = {'title': 'blahb blah', 'body': 'hehe haha'}

x = requests.post(url, json = myobj)
print(x.text)

r = requests.get('http://127.0.0.1:5000/posts')
print(r.text)

d = requests.delete("http://127.0.0.1:5000/posts/3")
print(d.status_code)
