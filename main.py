import requests
url = 'http://chatbottecblicnew.herokuapp.com/webhooks/rest/webhook'
myobj = {
"message":"hi",
"sender":"ABC"
}
x = requests.post(url, json = myobj)
print(x.text)
