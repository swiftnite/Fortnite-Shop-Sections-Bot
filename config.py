'''
The section below is your Twitter developer keys & tokens required for posting to your Twitter!

You must have a Twitter dev account which you can sign up for at https://developer.twitter.com/
Once signed up, apply for elevated access if you do not already have it (can be found under project one)
If accepted, go to overview (under projects & apps) and create a standalone app (The name of the app may be used as the source of the tweet eg. Twitter for iPhone)

Once created scroll to user authentication settings and click set up.
Inside you must select read and write permissions (permissions) and web app, automated app or bot (type).
For the required callback/redirect URL and website URL, the URL can be anything (you can even just use your Twitter eg. https://twitter.com/swiftnite)

Once saved, navigate to keys and tokens and regenerate API key and secret, fill these out in config.py (consumer_key and consumer_secret_key)
Navigate to keys and tokens again and generate Access token and secret, fill these out in config.py (access_token and access_token_secret)

Your app's permissions must have Read + Write or else it will not post!!
'''
class keys:
    consumer_key = ""
    consumer_secret_key = ""
    access_token = ""
    access_token_secret = ""
'''
The below section is for the customisation of the tweet itself
'''
class customisation:
    Heading: str = "Today's Shop Sections:" #NOTE: This will be the text displayed in the post above the sections
    Footer: str = "" #NOTE: This is what will appear under the sections! Leave blank("") if you do not want a footer
    Language: str = "en" #NOTE: This is the language that the sections are displayed in choose from ar / de / en / es / es-419 / fr / it / ja / ko / pl / pt-BR / ru / tr
    point: str = "- " #NOTE: This is the thing that will appear before the section name, For example, it would currently look like - Marvel (X7), you can change the "-" before the section name if you wish. NOTE: not everything works!!

    Brackets: bool = True #NOTE: THIS IS EITHER True or False! True means that the quantity will have brackets around it -> (X7) false means it won't -> X7
    showIfOne: bool = True #NOTE: THIS IS EITHER True or False! True means that the if the quantity of a section is one it will display 1 with your quantitySymbol. False means that the quantity will be hidden if 1!
    quantitySymbol: str = "x"  #NOTE: This is what will appear either before or after the quantity of that section. For example, X7 where this is "X". Another example is 7 tabs where this is " tabs"
    beforeOrAfter: str = "before" #NOTE: THIS IS EITHER "before" or "after"! Before means that the quantitySymbol will be before the quantity number of the sections
    sortMethod: str = "length" #NOTE: THIS IS EITHER "alphabetical" or "length"! Alphabetical means sections are sorted in alphabetical order, length means sections are sorted from shortest to longest
'''
If you have any issues please message me on Discord or Twitter and I will respond as quickly as possible!!
Twitter: @SwiftNite
Discord: Swift-nite#9078
'''
