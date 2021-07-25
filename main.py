from requests import get
from collections import Counter
import json
from time import sleep
import tweepy
import os, random
from PIL import Image, ImageDraw, ImageFont
from config import keys, customisation
consumer_key = keys.consumer_key
consumer_secret_key = keys.consumer_secret_key
access_token = keys.access_token
access_token_secret = keys.access_token_secret
Heading = customisation.Heading
Brackets = customisation.Brackets
point = customisation.point
image = customisation.image
auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def main():
    try:
        url=get('https://api.nitestats.com/v1/epic/modes-smart').json()
        url2=get('https://fortnitecontent-website-prod07.ol.epicgames.com/content/api/pages/fortnite-game').json()['shopSections']['sectionList']['sections']

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
                                if name.endswith('20'):
                                    name=name[:-2]
                                elif name.endswith('19'):
                                    name=name[:-2]
                                elif name.endswith('18'):
                                    name=name[:-2]
                                elif name.endswith('17'):
                                    name=name[:-2]
                                elif name.endswith('16'):
                                    name=name[:-2]
                                elif name.endswith('15'):
                                    name=name[:-2]
                                elif name.endswith('14'):
                                    name=name[:-2]
                                elif name.endswith('13'):
                                    name=name[:-2]
                                elif name.endswith('12'):
                                    name=name[:-2]
                                elif name.endswith('11'):
                                    name=name[:-2]
                                elif name.endswith('10'):
                                    name=name[:-2]
                                elif name.endswith('9'):
                                    name=name[:-1]
                                elif name.endswith('8'):
                                    name=name[:-1]
                                elif name.endswith('7'):
                                    name=name[:-1]
                                elif name.endswith('6'):
                                    name=name[:-1]
                                elif name.endswith('5'):
                                    name=name[:-1]
                                elif name.endswith('4'):
                                    name=name[:-1]
                                elif name.endswith('3'):
                                    name=name[:-1]
                                elif name.endswith('2'):
                                    name=name[:-1]
                                elif name.endswith('1'):
                                    name=name[:-1]
                                elif name.endswith('9B'):
                                    name=name[:-2]
                                elif name.endswith('8B'):
                                    name=name[:-2]
                                elif name.endswith('7B'):
                                    name=name[:-2]
                                elif name.endswith('6B'):
                                    name=name[:-2]
                                elif name.endswith('5B'):
                                    name=name[:-2]
                                elif name.endswith('4B'):
                                    name=name[:-2]
                                elif name.endswith('3B'):
                                    name=name[:-2]
                                elif name.endswith('2B'):
                                    name=name[:-2]
                                elif name.endswith('1B'):
                                    name=name[:-2]
                                elif name.endswith('B'):
                                    name=name[:-2]
                                elif name.endswith('9C'):
                                    name=name[:-2]
                                elif name.endswith('8C'):
                                    name=name[:-2]
                                elif name.endswith('7C'):
                                    name=name[:-2]
                                elif name.endswith('6C'):
                                    name=name[:-2]
                                elif name.endswith('5C'):
                                    name=name[:-2]
                                elif name.endswith('4C'):
                                    name=name[:-2]
                                elif name.endswith('3C'):
                                    name=name[:-2]
                                elif name.endswith('2C'):
                                    name=name[:-2]
                                elif name.endswith('1C'):
                                    name=name[:-2]
                                elif name.endswith('C'):
                                    name=name[:-2]
                            x.append(name)
                        else:
                            pass
                    if goatt==0:
                        name=a
                        if name.endswith('20'):
                            name=name[:-2]
                        elif name.endswith('19'):
                            name=name[:-2]
                        elif name.endswith('18'):
                            name=name[:-2]
                        elif name.endswith('17'):
                            name=name[:-2]
                        elif name.endswith('16'):
                            name=name[:-2]
                        elif name.endswith('15'):
                            name=name[:-2]
                        elif name.endswith('14'):
                            name=name[:-2]
                        elif name.endswith('13'):
                            name=name[:-2]
                        elif name.endswith('12'):
                            name=name[:-2]
                        elif name.endswith('11'):
                            name=name[:-2]
                        elif name.endswith('10'):
                            name=name[:-2]
                        elif name.endswith('9'):
                            name=name[:-1]
                        elif name.endswith('8'):
                            name=name[:-1]
                        elif name.endswith('7'):
                            name=name[:-1]
                        elif name.endswith('6'):
                            name=name[:-1]
                        elif name.endswith('5'):
                            name=name[:-1]
                        elif name.endswith('4'):
                            name=name[:-1]
                        elif name.endswith('3'):
                            name=name[:-1]
                        elif name.endswith('2'):
                            name=name[:-1]
                        elif name.endswith('1'):
                            name=name[:-1]
                        elif name.endswith('9B'):
                            name=name[:-2]
                        elif name.endswith('8B'):
                            name=name[:-2]
                        elif name.endswith('7B'):
                            name=name[:-2]
                        elif name.endswith('6B'):
                            name=name[:-2]
                        elif name.endswith('5B'):
                            name=name[:-2]
                        elif name.endswith('4B'):
                            name=name[:-2]
                        elif name.endswith('3B'):
                            name=name[:-2]
                        elif name.endswith('2B'):
                            name=name[:-2]
                        elif name.endswith('1B'):
                            name=name[:-2]
                        elif name.endswith('B'):
                            name=name[:-2]
                        elif name.endswith('9C'):
                            name=name[:-2]
                        elif name.endswith('8C'):
                            name=name[:-2]
                        elif name.endswith('7C'):
                            name=name[:-2]
                        elif name.endswith('6C'):
                            name=name[:-2]
                        elif name.endswith('5C'):
                            name=name[:-2]
                        elif name.endswith('4C'):
                            name=name[:-2]
                        elif name.endswith('3C'):
                            name=name[:-2]
                        elif name.endswith('2C'):
                            name=name[:-2]
                        elif name.endswith('1C'):
                            name=name[:-2]
                        elif name.endswith('C'):
                            name=name[:-2]
                        x.append(name)
                x=sorted(x)
                count=Counter(x)
                txt = open(f"sections.txt","w+")
                txti = open(f"sectionsi.txt","w+")
                txt.write(f"{Heading}\n")
                quant=0
                for i in count:
                    quantity=count[i]
                    name=i
                    if quantity!=1:
                        if Brackets == "True":
                            quantity=f" (X{quantity})"
                        elif Brackets == "False":
                            quantity=f" X{quantity}"
                        else:
                            quantity=f" (X{quantity})"
                        txt.write(f"\n{point}{name}{quantity}")
                        txti.write(f"{point}{name}{quantity}\n")
                        quant=quant+60
                    else:
                        txt.write(f"\n{point}{name}")
                        txti.write(f"{point}{name}\n")
                        quant=quant+60
                
                txt = open(f"sections.txt","r")
                file_contents = txt.read()
                print (file_contents)
                
                if image=='True':
                    quant=quant+100
                    background=random.choice(os.listdir("Backgrounds/")) 
                    backgrounds=Image.open(f'Backgrounds/{background}')
                    backgrounds=backgrounds.resize((500,quant))
                    FontSize = 80
                    while ImageFont.truetype(f"BurbankSmall-Black.otf", FontSize).getsize(f"Shop Sections!")[0] > 460:
                        FontSize -= 1
                    BurbankBigCondensed = ImageFont.truetype(f"BurbankSmall-Black.otf", FontSize)
                    textWidth = BurbankBigCondensed.getsize(f"Shop Sections!")[0]
                    Middle = int((500 - textWidth) / 2)
                    Draw = ImageDraw.Draw(backgrounds)
                    Draw.text((Middle, 20), (f"Shop Sections!"), (255, 255, 255), font=BurbankBigCondensed)
                    
                    txti = open(f"sectionsi.txt","r")
                    file = txti.readlines()
                    area=40
                    for i in file:
                        area+=60
                        i=i.rstrip()
                        FontSize = 40
                        while ImageFont.truetype(f"BurbankSmall-Black.otf", FontSize).getsize(f"{i}")[0] > 460:
                            FontSize -= 1
                        BurbankBigCondensed = ImageFont.truetype(f"BurbankSmall-Black.otf", FontSize)
                        textWidth = BurbankBigCondensed.getsize(f"{i}")[0]
                        Middle = int((500 - textWidth) / 2)
                        Draw = ImageDraw.Draw(backgrounds)
                        Draw.text((Middle, area), (f"{i}"), (255, 255, 255), font=BurbankBigCondensed)


                    backgrounds.save('sections.jpg')
                    pic='sections.jpg'
                    api.update_with_media(pic, f'{file_contents}')  
                else:
                    api.update_status(f"{file_contents}")
                print("Posted!")
                txt.close()
                txti.close()
                with open('Cache/cache1.json', 'w') as file:
                    json.dump(sections1, file, indent=3)
        except:
            pass            
    except:
        print("An error occured while checking for item shop sections!")

if __name__ == "__main__":
    while True:
        print("Checking for section changes!")
        main()
        sleep(20)
