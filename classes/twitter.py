import json
from time import sleep
try:
    import tweepy
except:
    print("The tweepy module is not installed!\nPlease run install.bat before running the bot\nAlternatively you can open command prompt and enter pip install tweepy")
    sleep(10)
    exit()

class twitterClass:
    def __init__(self, consumerKey, consumerSecretKey, accessToken, accessTokenSecret):
        if not all((consumerKey, consumerSecretKey, accessToken,accessTokenSecret)):
            print('WARNING!!!\nYou have not entered your Twitter Api keys into the config.py file!\nThis bot CANNOT run unless you enter these keys!!')
            sleep(10)
            exit()
        self.client = tweepy.Client(consumer_key=consumerKey,
                consumer_secret=consumerSecretKey,
                access_token=accessToken,
                access_token_secret=accessTokenSecret)

        auth = tweepy.OAuthHandler(consumerKey, consumerSecretKey)
        auth.set_access_token(accessToken, accessTokenSecret)

        self.api = tweepy.API(auth)

        try:
            account = self.api.verify_credentials(skip_status = True, include_email = False)
            hi = json.dumps(account._json)
            hi = json.loads(hi)
            self.twitter_tag = hi['screen_name']
            self.user = hi['name']
        except Exception as e:
            print(f'An error occurred verifying your api keys! Are they correct?\nActual error:\n{e}\n\n')

    def tweet(self, sections, imageEnabled, imagePath, imageType):
        if imageEnabled:
            media_list = []
            response = self.api.chunked_upload(filename=imagePath, file_type="image/"+imageType)
            media_list.append(response.media_id_string)

        tweetCount = 1
        for i in sections:
            i.encode('utf-8')
            print(i)
            if tweetCount==1:
                if (tweetCount == len(sections)) & (imageEnabled):
                    tweet = self.client.create_tweet(text = i, media_ids = media_list)
                else:
                    tweet = self.client.create_tweet(text = i)
                data = json.dumps(tweet.data)
                data = json.loads(data)
                id = data['id']
            else:
                try:
                    if (tweetCount == len(sections)) & (imageEnabled):
                        self.client.create_tweet(text = i, media_ids = media_list)
                        tweet = self.client.create_tweet(text = i, in_reply_to_tweet_id = id, media_ids = media_list)
                    else:
                        tweet = self.client.create_tweet(text = i, in_reply_to_tweet_id = id)
                    data = json.dumps(tweet.data)
                    data = json.loads(data)
                    id = data['id']
                except Exception as e:
                    print(f"\nAn error occured while replying with the extra sections!\n\nError:\n{e}\n\n")
            tweetCount += 1
        print("\nPosted!\n")
    
    def getUser(self):
        return self.user