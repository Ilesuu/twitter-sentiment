import tweepy


class TweetScraper:
    """ A class for retrieving tweet information from the twitter api"""
    def __init__(self, key):
        """ Initialize class by setting up twitter api authorisation

        :param key: name of file containing twitter api key. Should contain consumer API key, secret consumer api key,
        access token, and secret access token in that order each on their own line
        """
        f = open(key, "r")
        self.__auth = tweepy.OAuthHandler(f.readline().rstrip(), f.readline().rstrip())
        self.__auth.set_access_token(f.readline().rstrip(), f.readline().rstrip())
        self.__api = tweepy.API(self.__auth, wait_on_rate_limit=True)

    def test_key_validity(self):
        """ Test whether provided key is valid

        :return: bool indicating whether key was valid
        """
        try:
            self.__api.verify_credentials()
            return True
        except tweepy.TweepError:
            return False

    def get_tweet_texts(self, text_query, count):
        """ Search for tweets on twitter with a search term

        :param text_query: search term to be used
        :param count: amount of tweets to retrieve
        :return: list containing texts of all tweets retrieved
        """
        results = []
        tweets = self.__api.search(q=text_query, lang="en", count=count, tweet_mode='extended')
        for tweet in tweets:
            try:    # test if retweet
                results.append(tweet.retweeted_status.full_text)
            except AttributeError:  # Not a retweet
                results.append(tweet.full_text)
        return results
