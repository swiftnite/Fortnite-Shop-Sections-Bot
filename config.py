'''
The section below is your twitter develepor keys & tokens required for posting to your twitter!
You must have a twitter dev account of which you can apply for at https://developer.twitter.com/ 
You must create an app to acess your keys at https://developer.twitter.com/en/portal/projects-and-apps 
Whatever you name your app is what will appear as the source of where your tweet was posted from eg. Twitter for iPhone
Your apps permissions must have Read + Write or else it will not post!
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
    point: str = "- " #NOTE: This is the thing that will appear before the section name, For example it would currently look like - Marvel (X7), you can change the "-" before the section name if you wish. NOTE: not everything works!!

    Brackets: bool = True #NOTE: THIS IS EITHER True or False! True means that the quantity will have brackets around it -> (X7) false means it won't -> X7
    showIfOne: bool = True #NOTE: THIS IS EITHER True or False! True means that the if the quantity of a section is one it will display 1 with your quantitySymbol. False means that the quantity will be hidden if 1!
    quantitySymbol: str = "x"  #NOTE: This is what will appear either before or after the quantity of that section. For example X7 where this is "X". Another example is 7 tabs where this is " tabs"
    beforeOrAfter: str = "Before" #NOTE: THIS IS EITHER "Before" or "After"! Before means that the quantitySymbol will be before the quantity number of the sections
'''
If you have any issues please message me on discord or twitter and I will respond as quick as possible!!
Twitter: @SwiftNite
Discord: Swift-nite#9078
'''
