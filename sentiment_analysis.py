# A class for using azure api for evaluating sentiment in a dataset
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import statistics


class SentimentAnalysis:

    def __init__(self, api_info):
        f = open(api_info, "r")
        self.__key = f.readline().rstrip()
        self.__endpoint = f.readline().rstrip()
        self.__client = self.authenticate_client()

    def authenticate_client(self):
        ta_credential = AzureKeyCredential(self.__key)
        text_analytics_client = TextAnalyticsClient(
            endpoint=self.__endpoint,
            credential=ta_credential)
        return text_analytics_client

    def sentiment_analysis_example(self, documents):
        response = self.__client.analyze_sentiment(documents=documents,language="en")
        result = [doc for doc in response if not doc.is_error]
        positive = []
        neutral = []
        negative = []
        for doc in result:
            positive.append(doc.confidence_scores.positive)
            neutral.append(doc.confidence_scores.neutral)
            negative.append(doc.confidence_scores.negative)

        print("Total sentiment for topic: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
            statistics.mean(positive),
            statistics.mean(neutral),
            statistics.mean(negative)))
