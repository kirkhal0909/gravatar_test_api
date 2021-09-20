import requests
import hashlib
import sys

def emailMD5(email):
    hash_object = hashlib.md5(email.encode())
    return hash_object.hexdigest()

def getGravatarInfo(email):
    email_hash = emailMD5(email)
    json_link = "https://ru.gravatar.com/{}.json".format(email_hash)
    request = requests.get(json_link)
    result = request.json()['entry'][0]

    return {'result' : result}

if len(sys.argv) < 2:
    query = input("Enter email: ")
else:
    query = sys.argv[1]

result = getGravatarInfo(query)
print(result)