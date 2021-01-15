
from tweet_scraper import *
from sentiment_analysis import *
KEY_SOURCE = "access_key.txt"
SEARCH_COUNT = 100


def main():
    scraper = TweetScraper(KEY_SOURCE)
    if scraper.test_key_validity():
        print("API key validation successful")
        text_query = input("What term do you wish to search for?")
        test_list = scraper.get_tweet_texts(text_query, SEARCH_COUNT)
        for item in test_list:
            print("Tweet <", item, "> has ", analyze_text(item), " sentiment", sep="")
        print("Overall sentiment is ", analyze_dataset(test_list))
    else:
        print("API key validation failed")

main()
