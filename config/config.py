'''
The section below is your Twitter developer keys & tokens required for posting to your Twitter!

You must have a Twitter dev account which you can sign up for at https://developer.twitter.com/
Once signed up, apply for elevated access if you do not already have it (can be found under project one)
If accepted, go to overview (under projects & apps) and create a project.

Once you have created your app within the project scroll to user authentication settings inside the app and click set up.
Inside you must select read and write permissions (permissions) and web app, automated app or bot (type).
For the required callback/redirect URL and website URL, the URL can be anything (you can even just use your Twitter eg. https://twitter.com/swiftnite)

Once saved, navigate to keys and tokens and regenerate API key and secret, fill these out in config.py (consumerKey and consumerSecretKey respectively)
Navigate to keys and tokens again and generate Access token and secret, fill these out in config.py (accessToken and accessTokenSecret respectively)

Your app's permissions MUST have Read + Write or else it will not post!!
'''
class twitter:
    twitter = True #NOTE: This is either True or False. True means it will post to twitter!

    consumerKey = ""
    consumerSecretKey = ""
    accessToken = ""
    accessTokenSecret = ""
'''
The below section is for the customisation of the tweet itself
'''
class customisation:
    heading = "Today's Shop Sections:" #NOTE: This will be the text displayed in the post above the sections
    footer = "" #NOTE: This is what will appear under the sections! Leave blank("") if you do not want a footer
    language = "en" #NOTE: This is the language that the sections are displayed in choose from ar / de / en / es / es-419 / fr / it / ja / ko / pl / pt-BR / ru / tr
    point = "- " #NOTE: This is the thing that will appear before the section name, For example, it would currently look like - Marvel (X7), you can change the "-" before the section name if you wish.

    brackets = True #NOTE: THIS IS EITHER True or False! True means that the quantity will have brackets around it -> (X7) false means it won't -> X7
    showIfOne = True #NOTE: THIS IS EITHER True or False! True means that the if the quantity of a section is one it will display 1 with your quantitySymbol. False means that the quantity will be hidden if 1!
    quantitySymbol = "x"  #NOTE: This is what will appear either before or after the quantity of that section. For example, X7 where this is "X". Another example is 7 tabs where this is " tabs"
    beforeOrAfter = "before" #NOTE: THIS IS EITHER "before" or "after"! Before means that the quantitySymbol will be before the quantity number of the sections
    sortMethod = "length" #NOTE: THIS IS EITHER "alphabetical" or "length"! Alphabetical means sections are sorted in alphabetical order, length means sections are sorted from shortest to longest

    # It is NOT recommended you attach an image to the tweet however, if you REALLY want to... you can.
    image = "image.png" #NOTE: This is the filename for the image you want attached to the tweet (if imageEnabled is True). This is NOT recommended as it looks very bad when there are too many sections!!
    imageEnabled = False #NOTE: THIS IS EITHER True or False! True (NOT Recommended) means your image set above will be attached to the tweet (if there are many tweets it will be on the last one only!), False (Recommended) means no image
    imageFileType = "png" #NOTE: This is the media/mime type of the image. Examples: .bmp -> "bmp", .gif -> "gif", .jpeg/.jpg ->"jpeg", .png -> "png". See more here -> https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types (We are only interested in what is after image/)

    testMode = False #Do not touch this unless you need to generate the latest shop sections because you missed shop time
'''
Here you can change which api the bot uses!

The second api is always the official Epic Games API

For speed it is recommended to only enable one api.
However, if both are enabled the faster one is used.
'''
class api1:
    api = "https://api.nitestats.com/v1/epic/modes-smart" # NiteStats URL
    enabled = True

class api2:
    # FYI api = official epic games -> the bot will guide you through the setup process
    enabled = False #NOTE: THIS IS EITHER True or False! True will enable the use of the official Epic Games API
'''
If you require assistance or have suggestions you can join the Discord support server!
https://discord.gg/jHsAW2FKnj
'''