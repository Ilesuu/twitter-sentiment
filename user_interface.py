
from tweet_scraper import *
from sentiment_analysis import *
KEY_SOURCE = "access_key.txt"
SEARCH_COUNT = 100


class UserInterface:
    def __init__(self):
        self.__continue_loop = True
        self.__scraper = TweetScraper(KEY_SOURCE)
        if self.__scraper.test_key_validity():
            print("API key successfully valid")
            self.main_loop()
        else:
            print("No valid API key")
            self.exit()

    def main_loop(self):
        while self.__continue_loop:
            command = input("Type a to analyze sentiment for a keyword, type q to quit: ")
            if command == "a":
                self.analyze_sentiment()
            elif command == "q":
                self.exit()
            else:
                print("Unknown command")

    def analyze_sentiment(self):
        text_query = input("What do you term do you want to analyze? ")
        try:
            results = self.__scraper.get_tweet_texts(text_query, SEARCH_COUNT)
            print("Overall sentiment is ", analyze_dataset(results))
        except tweepy.RateLimitError:
            print("Too many API requests, wait at least 15 minutes before trying again")

    def exit(self):
        self.__continue_loop = False
        print("Exiting program")
