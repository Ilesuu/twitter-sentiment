from tweet_scraper import *
from sentiment_analysis import *

# file containing twitter api key
TWITTER_KEY_SOURCE = "access_key.txt"

AZURE_KEY_SOURCE = "azure_key.txt"
# Amount of tweets to retrieve per search, my azure API key does not allow for many, so this is quite small
SEARCH_COUNT = 50


class UserInterface:
    """ Class providing user interface for the twitter sentiment analysis"""
    def __init__(self):
        self.__continue_loop = True
        self.__scraper = TweetScraper(TWITTER_KEY_SOURCE)
        self.__analysis = SentimentAnalysis(AZURE_KEY_SOURCE)
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
            # Formatting results to get as much data as possible for azure api
            formatted_results = []
            i = 0
            for x in range(0, 5):
                formatted_string = ""
                for y in range(0, 10):
                    if i < len(results):
                        formatted_string += results[i]
                        i += 1
                formatted_results.append(formatted_string)

            self.__analysis.sentiment_analysis_example(formatted_results)

        except tweepy.RateLimitError:
            print("Too many API requests, wait at least 15 minutes before trying again")

    def exit(self):
        """ Stop main loop, ending the program"""
        self.__continue_loop = False
        print("Exiting program")
