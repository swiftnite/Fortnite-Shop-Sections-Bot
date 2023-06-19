import json
from datetime import datetime
import pytz
from tzlocal import get_localzone
import requests

class authClass:
    def readAuth(self):
        with open('cache/auth.json', 'r') as autho:
            self.authFile = json.load(autho)

    def writeAuth(self):
        with open('cache/auth.json', 'w') as file:
            json.dump(self.authFile, file, indent=3)

    def __init__(self):
        self.readAuth()
        if not all((self.authFile['deviceId'], self.authFile ['accountId'], self.authFile ['secret'], self.authFile ['access_token'], self.authFile ['expires_at'])):
            self.generateAuth()

    def authCheck(self):
        expiry = self.authFile['expires_at']
        expiry = expiry.split(".")[0]
        expiry = expiry.split("T")
        self.expiry = f"{expiry[0]} {expiry[1]}"

        dt_tuple = tuple([int(x) for x in self.expiry[:10].split('-')])+tuple([int(x) for x in self.expiry[11:].split(':')])
        my_date = datetime(*dt_tuple, tzinfo=pytz.utc)
        local_tz = get_localzone() 
        my_date = my_date.astimezone(local_tz)
        now_utc = datetime.now(local_tz)
        self.expires = my_date.replace(minute=5*(my_date.minute // 5)).strftime('%Y-%m-%d %H:%M')
        self.current = now_utc.strftime('%Y-%m-%d %H:%M')

        try:
            if (self.current > self.expires) or (self.current == self.expires):
                print(f"Generating new token -  {self.current}")
                try:
                    auth = requests.post('https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token', data=f"grant_type=device_auth&account_id={self.authFile['accountId']}&device_id={self.authFile['deviceId']}&secret={self.authFile['secret']}", headers={
                                        "Content-Type": "application/x-www-form-urlencoded", "Authorization": "basic MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE="})
                    bearer = auth.json()['access_token']
                    expiry = auth.json()['expires_at']
                    self.authFile['expires_at'] = expiry
                    self.authFile['access_token'] = bearer
                    self.writeAuth()
                    print(f'Auth token updated - {self.current}')
                except Exception as e:
                    print(f'AUTH GENERATION ERROR!!\n{e}')
                    self.generateAuth()
                    
        except IndexError as e:
            self.generateAuth()
        except Exception as e:
            print(f'AUTH GENERATION ERROR!!\n{e}')

    def generateAuth(self):
        url = 'https://www.epicgames.com/id/api/redirect?clientId=3446cd72694c4a4485d81b77adbb2141&responseType=code'

        print(f'Epic Games Auth Setup!')
        print(f'1. Please login to Epic Games in your web browser (An alt account is recommended)')
        print(f'2. Head to the following link:\n{url}')
        print(f'3. Copy the authorizationCode value')

        authorizationCode = input("authorizationCode: ")

        # Step 1 (Initial auth)
        headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "basic MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE="}
        stepone = requests.post(url='https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token', data=f"grant_type=authorization_code&code={authorizationCode}", headers=headers).json()
        access_token = stepone['access_token']
        account_id = stepone['account_id']

        self.authFile['access_token'] = stepone['access_token']
        self.authFile['expires_at'] = stepone['expires_at']

        # Step 2 (Device id)
        headers = {"Authorization": f"Bearer {access_token}"}
        steptwo = requests.post(url = f'https://account-public-service-prod.ol.epicgames.com/account/api/public/account/{account_id}/deviceAuth', headers=headers).json()

        self.authFile['deviceId'] = steptwo['deviceId']
        self.authFile['accountId'] = steptwo['accountId']
        self.authFile['secret'] = steptwo['secret']

        with open('cache/auth.json', 'w') as file:
            json.dump(self.authFile, file, indent=3)
        expiry = self.authFile['expires_at'].split(".")[0]
        expiry = expiry.split("T")
        self.expiry = f"{expiry[0]} {expiry[1]}"

        dt_tuple = tuple([int(x) for x in self.expiry[:10].split('-')])+tuple([int(x) for x in self.expiry[11:].split(':')])
        my_date = datetime(*dt_tuple, tzinfo=pytz.utc)
        local_tz = get_localzone() 
        my_date = my_date.astimezone(local_tz)
        now_utc = datetime.now(local_tz)
        self.expires = my_date.replace(minute=5*(my_date.minute // 5)).strftime('%Y-%m-%d %H:%M')
        self.current = now_utc.strftime('%Y-%m-%d %H:%M')