'''
The section below is your Twitter developer keys & tokens required for posting to your Twitter!

You must have a Twitter dev account which you can sign up for at https://developer.twitter.com/
Once signed up, apply for elevated access if you do not already have it (can be found under project one)
If accepted, go to overview (under projects & apps) and create an app.
-> For v2 users this can be created when creating your project, v1 users can create a standalone app. (Either way works)
-> Do not worry about the initial keys it gives you

Once you have created your app scroll to user authentication settings inside the app and click set up.
Inside you must select read and write permissions (permissions) and web app, automated app or bot (type).
For the required callback/redirect URL and website URL, the URL can be anything (you can even just use your Twitter eg. https://twitter.com/swiftnite)

Once saved, navigate to keys and tokens and regenerate API key and secret, fill these out in config.py (consumerKey and consumerSecretKey respectively)
Navigate to keys and tokens again and generate Access token and secret, fill these out in config.py (accessToken and accessTokenSecret respectively)

Your app's permissions MUST have Read + Write or else it will not post!!
'''
class keys:
    consumerKey: str = ""
    consumerSecretKey: str = ""
    accessToken: str = ""
    accessTokenSecret: str = ""

    twitterBlue: bool = False #NOTE: THIS IS True OR False! IF YOU HAVE TWITTER BLUE SET THIS TO True!!!!
'''
The below section is for the customisation of the tweet itself
'''
class customisation:
    heading: str = "Today's Shop Sections:" #NOTE: This will be the text displayed in the post above the sections
    footer: str = "" #NOTE: This is what will appear under the sections! Leave blank("") if you do not want a footer
    language: str = "en" #NOTE: This is the language that the sections are displayed in choose from ar / de / en / es / es-419 / fr / it / ja / ko / pl / pt-BR / ru / tr
    point: str = "- " #NOTE: This is the thing that will appear before the section name, For example, it would currently look like - Marvel (X7), you can change the "-" before the section name if you wish.

    brackets: bool = True #NOTE: THIS IS EITHER True or False! True means that the quantity will have brackets around it -> (X7) false means it won't -> X7
    showIfOne: bool = True #NOTE: THIS IS EITHER True or False! True means that the if the quantity of a section is one it will display 1 with your quantitySymbol. False means that the quantity will be hidden if 1!
    quantitySymbol: str = "x"  #NOTE: This is what will appear either before or after the quantity of that section. For example, X7 where this is "X". Another example is 7 tabs where this is " tabs"
    beforeOrAfter: str = "before" #NOTE: THIS IS EITHER "before" or "after"! Before means that the quantitySymbol will be before the quantity number of the sections
    sortMethod: str = "length" #NOTE: THIS IS EITHER "alphabetical" or "length"! Alphabetical means sections are sorted in alphabetical order, length means sections are sorted from shortest to longest

    # It is NOT recommended you attatch an image to the tweet however, if you REALLY want to... you can.
    image: str = "image.png" #NOTE: This is the filename for the image you want attatched to the tweet (if imageEnabled is True). This is NOT recommended as it looks very bad when there are too many sections!!
    imageEnabled: bool = False #NOTE: THIS IS EITHER True or False! True (NOT Recommended) means your image set above will be attatched to the tweet (if there are many tweets it will be on the last one only!), False (Recommended) means no image
    imageFileType: str = "png" #NOTE: This is the media/mime type of the image. Examples: .bmp -> "bmp", .gif -> "gif", .jpeg/.jpg ->"jpeg", .png -> "png". See more here -> https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types (We are only interested in what is after image/)
'''
Here you can change which api the bot uses!

The second api is always the official Epic Games API
however you can disable it if you do not wish to use it
'''
class api1:
    api: str = "https://api.nitestats.com/v1/epic/modes-smart" # NiteStats URL

class api2:
    enabled: bool = True #NOTE: THIS IS EITHER True or False! True will enable the use of the official Epic Games API, initial setup will be required if this is enabled!
'''
If you require assistance or have suggestions you can:
- Join the Discord support server -> https://discord.gg/jHsAW2FKnj
- Message me on Twitter -> https://twitter.com/intent/follow?screen_name=SwiftNite
- Create a GitHub discussion -> https://github.com/swiftnite/Fortnite-Shop-Sections-Bot/discussions/new/choose
'''