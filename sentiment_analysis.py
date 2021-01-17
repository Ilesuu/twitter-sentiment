# Simple functions for evaluating positive or negative sentiment in a text or dataset

# Positive keywords to be searched for
KEYWORDS_POSITIVE = ["good", "strong", "great", "nice", "awesome", "cool", "thank", "thanks", "love", "win",
                     "wonderful", "beautiful", "perfect"]
# Negative keywords to be searched for
KEYWORDS_NEGATIVE = ["bad", "weak", "terrible", "shit", "hate", "lose", "war", "terrorist", "dictator", "poison",
                     "scandal", "hoax", "worst", "disgrace", "dead"]


def analyze_text(text):
    """
    Analyze sentiment within a single text sample
    :param text: string to be analyzed
    :return: string containing sentiment of the text( Negative, Neutral or Positive)
    """
    positive_words = 0
    negative_words = 0

    # Test how many negative and positive keywords the text contains
    for word in KEYWORDS_POSITIVE:
        if word in text.lower():
            positive_words += 1
    for word in KEYWORDS_NEGATIVE:
        if word in text.lower():
            negative_words += 1

    # Return appropriate response
    if positive_words > negative_words:
        return "Positive"
    elif negative_words > positive_words:
        return "Negative"
    else:
        return "Neutral"


def analyze_dataset(dataset):
    """
    Analyze sentiment for a list of strings
    :param dataset: list containing strings to be analyzed
    :return: string containing sentiment of the dataset( Negative, Neutral or Positive)
    """
    positive_amount = 0
    negative_amount = 0

    # Test sentiment for each text in the dataset using the analyze_text function
    for text in dataset:
        sentiment = analyze_text(text)
        if sentiment == "Positive":
            positive_amount += 1
        elif sentiment == "Negative":
            negative_amount += 1

    # Return appropriate response
    if positive_amount > negative_amount:
        return "Positive"
    elif negative_amount > positive_amount:
        return "Negative"
    else:
        return "Neutral"

