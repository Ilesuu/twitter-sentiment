
KEYWORDS_POSITIVE = ["good", "strong", "great", "nice", "awesome", "cool", "thank", "thanks", "love", "win",
                     "wonderful", "beautiful", "perfect"]
KEYWORDS_NEGATIVE = ["bad", "weak", "terrible", "shit", "hate", "lose"]


def analyze_text(text):
    positive_words = 0
    negative_words = 0
    for word in KEYWORDS_POSITIVE:
        if word in text.lower():
            positive_words += 1
    for word in KEYWORDS_NEGATIVE:
        if word in text.lower():
            negative_words += 1

    if positive_words > negative_words:
        return "Positive"
    elif negative_words > positive_words:
        return "Negative"
    else:
        return "Neutral"


def analyze_dataset(dataset):
    positive_amount = 0
    negative_amount = 0
    for text in dataset:
        sentiment = analyze_text(text)
        if sentiment == "Positive":
            positive_amount += 1
        elif sentiment == "Negative":
            negative_amount += 1

    if positive_amount > negative_amount:
        return "Positive"
    elif negative_amount > positive_amount:
        return "Negative"
    else:
        return "Neutral"

