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

    def get_tweet_texts(self, text_query, count):
        results = []
        tweets = self.__api.search(q=text_query, lang="en", count=count, tweet_mode='extended')
        for tweet in tweets:
            try:    # test if retweet
                results.append(tweet.retweeted_status.full_text)
            except AttributeError:  # Not a retweet
                results.append(tweet.full_text)
        return results
