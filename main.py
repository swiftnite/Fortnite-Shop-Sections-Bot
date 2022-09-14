from requests import get
from collections import Counter
import json
from time import sleep
import tweepy
from config import keys, customisation
consumer_key = keys.consumer_key
consumer_secret_key = keys.consumer_secret_key
access_token = keys.access_token
access_token_secret = keys.access_token_secret
if not all((consumer_key, consumer_secret_key, access_token,access_token_secret)):
    print('WARNING!!!\nYou have not entered your Twitter Api keys into the config.json file!\nThis bot will be unable to post unless you enter these keys.\n\n')

Heading = customisation.Heading
Footer = customisation.Footer
Language = customisation.Language
point = customisation.point

Brackets = customisation.Brackets
showIfOne = customisation.showIfOne
quantitySymbol = customisation.quantitySymbol
beforeOrAfter = customisation.beforeOrAfter

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
with open('translations.json', 'r', encoding='utf8') as translator:
    translator = json.load(translator)
sFix1=["20", "19", "18", "17", "16", "15", "14", "13", "12", "11", "10", "9B", "8B", "7B", "6B", "5B", "4B", "3B", "2B", "1B", "9C", "8C", "7C", "6C", "5C", "4C", "3C", "2C", "1C"]
sFix2=["9", "8", "7", "6", "5", "4", "3", "2", "1", "B", "C"]

def main():
    try:
        url=get('https://api.nitestats.com/v1/epic/modes-smart').json()
        url2=get(f'https://fortnitecontent-website-prod07.ol.epicgames.com/content/api/pages/fortnite-game/shop-sections?lang={Language}').json()['sectionList']['sections']
        try:
            sections1=url['channels']['client-events']['states'][1]['state']['sectionStoreEnds']
            x = []
            txt = open(f"sections.txt","w+")
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth)
            with open('Cache/cache1.json', 'r') as cache:
                cache1 = json.load(cache)
            if sections1 != cache1:
                for a in sections1:

                    goatt=0
                    for b in url2:
                        name=a
                        sectionId=b['sectionId']
                        if name==sectionId:
                            goatt+=1
                            try:
                                name=b['sectionDisplayName']
                            except:
                                name=a
                                for o in translator:
                                    if name.startswith(o):
                                        name=translator[o][Language]
                                        success=True
                                    else:
                                        success=False
                                if success==False:
                                    if name.endswith(tuple(sFix1)):
                                        name=name[:-2]
                                    elif name.endswith(tuple(sFix2)):
                                        name=name[:-1]
                            x.append(name)
                        else:
                            pass
                    if goatt==0:
                        name=a
                        for o in translator:
                            if name.startswith(o):
                                name=translator[o][Language]
                                success=True
                            else:
                                success=False
                        if success==False:
                            if name.endswith(tuple(sFix1)):
                                name=name[:-2]
                            elif name.endswith(tuple(sFix2)):
                                name=name[:-1]
                        x.append(name)
                x=sorted(x)
                count=Counter(x)
                txt = open(f"sections.txt","wb")
                txt.write(f"{Heading}\n".encode('utf-8'))
                quant=0
                for i in count:
                    quantity=count[i]
                    name=i
                    if quantity!=1:
                        if beforeOrAfter=="after":
                            if Brackets == False:
                                quantity=f" {quantity}{quantitySymbol}"
                            else:
                                quantity=f" ({quantity}{quantitySymbol})"
                            txt.write(f"\n{point}{name}{quantity}".encode('utf-8'))
                        else:
                            if Brackets == False:
                                quantity=f" {quantitySymbol}{quantity}"
                            else:
                                quantity=f" ({quantitySymbol}{quantity})"
                            txt.write(f"\n{point}{name}{quantity}".encode('utf-8'))
                        
                    else:
                        if showIfOne==True:
                            if beforeOrAfter=="after":
                                if Brackets == False:
                                    quantity=f" {quantity}{quantitySymbol}"
                                else:
                                    quantity=f" ({quantity}{quantitySymbol})"
                                txt.write(f"\n{point}{name}{quantity}".encode('utf-8'))
                            else:
                                if Brackets == False:
                                    quantity=f" {quantitySymbol}{quantity}"
                                else:
                                    quantity=f" ({quantitySymbol}{quantity})"
                                txt.write(f"\n{point}{name}{quantity}".encode('utf-8'))
                        else:
                            txt.write(f"\n{point}{name}".encode('utf-8'))
                if Footer!="":
                    txt.write(f"\n\n{Footer}".encode('utf-8'))
                txt.close()
                txt = open(f"sections.txt","r", encoding='utf8')
                file_contents = txt.read()
                print (file_contents)
                api.update_status(f"{file_contents}")
                print("Posted!")
                txt.close()
                with open('Cache/cache1.json', 'w') as file:
                    json.dump(sections1, file, indent=3)
        except:
            pass            
    except Exception as e:
        print("An error occured while checking for item shop sections!\n\n{e}")

if __name__ == "__main__":
    while True:
        print("Checking for section changes!")
        main()
        sleep(20)
