
from tweet_scraper import *
KEY_SOURCE = "access_key.txt"


def main():
    scraper = TweetScraper(KEY_SOURCE)
    if scraper.test_key_validity():
        print("Success")
    else:
        print("Fail")


main()
