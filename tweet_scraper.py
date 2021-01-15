#

import tweepy



class TweetScraper:
    def __init__(self, key):
        f = open(key, "r")
        self.__auth = tweepy.OAuthHandler(f.readline().rstrip(), f.readline().rstrip())
        self.__auth.set_access_token(f.readline().rstrip(), f.readline().rstrip())
        self.__api = tweepy.API(self.__auth, wait_on_rate_limit=True)

    def test_key_validity(self):
        try:
            self.__api.verify_credentials()
            return True
        except tweepy.TweepError:
            return False
