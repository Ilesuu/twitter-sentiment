from tweet_scraper import *
from sentiment_analysis import *

# file containing twitter api key
KEY_SOURCE = "access_key.txt"
# Amount of tweets to retrieve per search
SEARCH_COUNT = 1000


class UserInterface:
    """ Class providing user interface for the twitter sentiment analysis"""
    def __init__(self):
        self.__continue_loop = True
        self.__scraper = TweetScraper(KEY_SOURCE)
        if self.__scraper.test_key_validity():          # Test whether provided api key works
            print("API key successfully validated")
            self.main_loop()
        else:                                           # If key does not work exit program
            print("No valid API key")
            self.exit()

    def main_loop(self):
        """ Main program loop. Continues until the exit method is called"""
        while self.__continue_loop:
            command = input("Type a to analyze sentiment for a keyword, type q to quit: ")
            if command == "a":
                self.analyze_sentiment()
            elif command == "q":
                self.exit()
            else:
                print("Unknown command")

    def analyze_sentiment(self):
        """ Method for analyzing sentiment on a chosen keyword. Prints results"""
        text_query = input("What do you term do you want to analyze? ")
        try:
            results = self.__scraper.get_tweet_texts(text_query, SEARCH_COUNT)
            print("Overall sentiment is ", analyze_dataset(results))
        except tweepy.RateLimitError:
            print("Too many API requests, wait at least 15 minutes before trying again")

    def exit(self):
        """ Stop main loop, ending the program"""
        self.__continue_loop = False
        print("Exiting program")
