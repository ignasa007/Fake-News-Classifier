import tweepy

def getText(url):

    consumer_key = "7FuNEf5ftMvWW8pUKdRABpRy1"
    consumer_key_secret = "R4Srk1XN8Zx7RnkgCpBUY6RMayS9gNRCIWuMXj8fEsHWDlkazB"
    access_token = "1251237261162582018-GLY1GDryQ6poJ3oNl1Wgxvs9h0Bgpk"
    access_token_secret = "3EBhOHb3Wq2BYrDUw1fl5x9OU59Kry35OWLYbhipn7gWw"

    auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tweetID = url.split("/")[-1].split("?")[0]

    try:
        tweetFetched = api.get_status(tweetID, tweet_mode="extended")
        txt = (" ").join(tweetFetched.full_text.split(" ")[:-1])
        return txt
    except Exception as e:
        print(e)