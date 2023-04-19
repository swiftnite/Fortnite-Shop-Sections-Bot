#####################
debug = False
####################

try:
    from requests import get
except:
    print("The requests module is not installed!\nPlease run install.bat before running the bot\nAlternatively you can open command prompt and enter pip install requests")
    sleep(10)
    exit()

try:
    import tweepy
except:
    print("The tweepy module is not installed!\nPlease run install.bat before running the bot\nAlternatively you can open command prompt and enter pip install tweepy")
    sleep(10)
    exit()

try:
    import emoji
except:
    print("The emoji module is not installed!\nPlease run install.bat before running the bot\nAlternatively you can open command prompt and enter pip install emoji")
    sleep(10)
    exit()
try:
    from dateutil.parser import parse
except:
    print("The python-dateutil module is not installed!\nPlease run install.bat before running the bot\nAlternatively you can open command prompt and enter pip install python-dateutil")
    sleep(10)
    exit()

from collections import Counter
import json
from time import sleep
from config import keys, customisation, api1, api2

consumer_key = keys.consumer_key
consumer_secret_key = keys.consumer_secret_key
access_token = keys.access_token
access_token_secret = keys.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

if not all((consumer_key, consumer_secret_key, access_token,access_token_secret)):
    print('WARNING!!!\nYou have not entered your Twitter Api keys into the config.py file!\nThis bot CANNOT run unless you enter these keys!!')
    sleep(10)
    exit()

try:
    account = api.verify_credentials(skip_status=True,include_email=False)
    hi = json.dumps(account._json)
    hi = json.loads(hi)
    twitter_tag = hi['screen_name']
    user = hi['name']
except Exception as e:
    print(f'An error occurred verifying your api keys! Are they correct?\nActual error:\n{e}\n\n')

Heading = customisation.Heading
Footer = customisation.Footer
point = customisation.point
Language = customisation.Language

specialLangs = ['ja', 'zh-cn', 'zh-hant', 'ko']

# As Chinese, Japanese and Korean glyphs count as 2 characters,
# tweet character limit is only 140 for these languages
if Language.lower() in specialLangs:
    defaultCharLimit = 140
else:
    defaultCharLimit = 280

headingEmojis = 0
footerEmojis = 0

for c in Heading:
    if emoji.is_emoji(c):
        headingEmojis+=1

for c in Footer:
    if emoji.is_emoji(c):
        footerEmojis+=1

Brackets = customisation.Brackets
showIfOne = customisation.showIfOne
quantitySymbol = customisation.quantitySymbol
beforeOrAfter = customisation.beforeOrAfter
sortMethod = customisation.sortMethod

def magicalSortingFunction(section):
    return section["length"], section["count"]

with open('translations.json', 'r', encoding='utf8') as translator:
    translator = json.load(translator)

sFix1=["20", "19", "18", "17", "16", "15", "14", "13", "12", "11", "10", "9B", "8B", "7B", "6B", "5B", "4B", "3B", "2B", "1B", "9C", "8C", "7C", "6C", "5C", "4C", "3C", "2C", "1C"]
sFix2=["9", "8", "7", "6", "5", "4", "3", "2", "1", "B", "C"]

print(f"\nWelcome {user} to SwiftNite's shop sections bot!\n\nFeel free to follow me on twitter -> @SwiftNite\nUse code Swift-Nite in Fortnite and the Epic Games Store to support me and this shop sections bot!\n\n\nThe bot is now looking for new shop sections!\n")

def main():
    try:
        try:
            if api1.api == "https://fn-api.com/api/calendar":
                apione = get(api1.api).json()['data']
            else:
                apione=get(api1.api).json()
            time1 = parse(apione['currentTime'])
        except Exception as e:
            time1 = parse("1989-12-13T00:00:00.000Z")

            if debug==True:
                print(f"Error (api 1):\n{e}")

        if api2.enabled==True:
            try:
                if api2.api == "https://fn-api.com/api/calendar":
                    apitwo = get(api2.api).json()['data']
                else:
                    apitwo=get(api2.api).json()
                time2 = parse(apitwo['currentTime'])
            except Exception as e:
                time2 = parse("1989-12-13T00:00:00.000Z")

                if debug==True:
                    print(f"Error (api 2):\n{e}")

            if time1 < time2:
                url = apione
            else:
                url = apitwo
        else:
            url = apione

        url2=get(f'https://fortnitecontent-website-prod07.ol.epicgames.com/content/api/pages/fortnite-game/shop-sections?lang={Language}').json()['sectionList']['sections']
        try:
            sections1=url['channels']['client-events']['states'][1]['state']['sectionStoreEnds']

            x = []
            toSort = []

            # Each tweet will be stored in this array. Usually just one tweet is needed
            # however if it goes over the character limit then a reply is made with the
            # extra sections
            txt = []
            txt.append(f"{Heading}\n")

            with open('cache.json', 'r') as cache:
                cache1 = json.load(cache)

            if sections1 != cache1:
                for a in sections1:
                    goatt=0
                    for b in url2:
                        error = False
                        name=a
                        sectionId=b['sectionId']
                        if name==sectionId:
                            goatt+=1
                            try:
                                if b['sectionDisplayName']:
                                    name = b['sectionDisplayName']
                                else:
                                    error = True
                            except:
                                error = True
                            if error == True:
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
                count=Counter(x)
                for i in count:
                    quantity=count[i]
                    name=i
                    if quantity!=1:
                        if beforeOrAfter=="after":
                            if Brackets == False:
                                quantity=f" {quantity}{quantitySymbol}"
                            else:
                                quantity=f" ({quantity}{quantitySymbol})"
                            
                        else:
                            if Brackets == False:
                                quantity=f" {quantitySymbol}{quantity}"
                            else:
                                quantity=f" ({quantitySymbol}{quantity})"
                        toSort.append(f"{point}{name}{quantity}")
                        
                    else:
                        if showIfOne==True:
                            if beforeOrAfter=="after":
                                if Brackets == False:
                                    quantity=f" {quantity}{quantitySymbol}"
                                else:
                                    quantity=f" ({quantity}{quantitySymbol})"
                            else:
                                if Brackets == False:
                                    quantity=f" {quantitySymbol}{quantity}"
                                else:
                                    quantity=f" ({quantitySymbol}{quantity})"

                            toSort.append(f"{point}{name}{quantity}")
                        else:
                            toSort.append(f"n{point}{name}")
                if sortMethod == "alphabetical":
                    sort = sorted(toSort)
                else:
                    sortList = []
                    sort = ""
                    count = 1
                    for i in toSort:
                        sortList.append({"name": i, "length": len(i), "count": count})
                        count+=1
                    sortList.sort(key=magicalSortingFunction)
                    sort = []
                    for i in sortList:
                        sort.append(i["name"])


                for i in sort:
                    if Heading in txt[-1]:
                        if len(txt[-1]) + len(f"\n{i}") + headingEmojis > defaultCharLimit:
                            txt.append(f"\n{i}")
                        else:
                            txt[-1] += f"\n{i}"
                    else:
                        if len(txt[-1]) + len(f"\n{i}") > defaultCharLimit:
                            txt.append(f"\n{i}")
                        else:
                            txt[-1] += f"\n{i}"
                
                if Footer!="":
                    if len(txt[-1])+ len(f"\n\n{Footer}") + footerEmojis < defaultCharLimit:
                        txt[-1] += f"\n\n{Footer}"
                    
                tweetCount = 1
                for i in txt:
                    i.encode('utf-8')
                    print(i)
                    if tweetCount==1:
                        tweet = api.update_status(i)
                        hi = json.dumps(tweet._json)
                        hi = json.loads(hi)
                        id = hi['id_str']
                    else:
                        try:
                            tweet = api.update_status(status=f"@{twitter_tag} {i}", in_reply_to_status_id=id)
                            hi = json.dumps(tweet._json)
                            hi = json.loads(hi)
                            id = hi['id_str']
                        except Exception as e:
                            print(f"\nAn error occured while replying with the extra sections!\n\nError:\n{e}\n\n")
                    tweetCount+=1
                print("\nPosted!\n")
                with open('cache.json', 'w') as file:
                    json.dump(sections1, file, indent=3)
        except Exception as e:
            if debug==True:
                print(f"\nError:\n{e}\n")
            else:
                pass
    except Exception as e:
        print(f"\nAn error occured while checking for item shop sections!\n\n{e}")

if __name__ == "__main__":
    while True:
        main()
        sleep(15)
