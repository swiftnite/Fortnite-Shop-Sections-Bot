from time import sleep

# Module imports
# Includes extra error catching for a better user experience
# (Used in classes but easier to check if they are installed here)

try:
    import requests
except:
    print("The requests module is not installed!\nPlease run install.bat before running the bot\nAlternatively you can open command prompt and enter pip install requests")
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
try:
    from datetime import datetime
except:
    print("The DateTime module is not installed!\nPlease run install.bat before running the bot\nAlternatively you can open command prompt and enter pip install DateTime")
    sleep(10)
    exit()
try:
    import pytz
except:
    print("The pytz module is not installed!\nPlease run install.bat before running the bot\nAlternatively you can open command prompt and enter pip install pytz")
    sleep(10)
    exit()
try:
    from tzlocal import get_localzone
except:
    print("The tzlocal module is not installed!\nPlease run install.bat before running the bot\nAlternatively you can open command prompt and enter pip install tzlocal")
    sleep(10)
    exit()

from config.config import twitter, customisation, api1, api2
from classes.twitter import twitterClass
from classes.sections import sectionsClass
from classes.auth import authClass

if (api1.enabled == False) & (api2.enabled == False):
    print("Please enable at least one api!\nHow would the bot run without them??")

sectionsInit = sectionsClass(customisation, api1.api, api1.enabled, api2.enabled)

if api2.enabled:
    authInit = authClass()
else:
    authInit = None

if twitter.twitter:
    twitterInit = twitterClass(twitter.consumerKey, twitter.consumerSecretKey, twitter.accessToken, twitter.accessTokenSecret)
    user = twitterInit.getUser()
    print(f"\nWelcome {user} to SwiftNite's shop sections bot!\n\nFeel free to follow me on twitter -> @SwiftNite\nUse code Swift-Nite in Fortnite and the Epic Games Store to support me and this shop sections bot!\n\n\nThe bot is now looking for new shop sections!\n")
else:
    print(f"\nWelcome to SwiftNite's shop sections bot!\n\nFeel free to follow me on twitter -> @SwiftNite\nUse code Swift-Nite in Fortnite and the Epic Games Store to support me and this shop sections bot! #EpicPartner\n\n\nThe bot is now looking for new shop sections!\n")

def main():
    sectionsInit.pickApi(authInit)
    sections = sectionsInit.sections() 

    if (sections != None) & (twitter.twitter):
        print("Tweeting new shop sections!")
        twitterInit.tweet(sections, customisation.imageEnabled, customisation.image, customisation.imageFileType)

    elif  (sections != None) & (twitter.twitter == False):
        for i in sections:
            i.encode('utf-8')
            print(i)

if __name__ == "__main__":
    while True:
        if api2.enabled:
            authInit.authCheck()
        main()
        sleep(15)