import re


def analyze_review_sentiment() -> None:
    """Reads a review from the console and prints whether it is Positive or Negative.

    The analysis is keyword-based with simple negation handling (e.g., "not good").
    """
    review_text = input("Enter your review: ")
    review_text_lower = review_text.lower()

    positive_words = {
        "good", "great", "excellent", "amazing", "awesome", "fantastic", "love",
        "liked", "wonderful", "positive", "pleasant", "satisfied", "happy",
        "recommend", "best", "perfect", "nice", "enjoyed", "cool"
    }
    negative_words = {
        "bad", "terrible", "awful", "horrible", "worst", "poor", "hate",
        "dislike", "boring", "disappointing", "negative", "sad", "angry",
        "waste", "problem", "bugs", "buggy", "slow", "annoying"
    }

    # Basic tokenization on words
    tokens = re.findall(r"[a-zA-Z']+", review_text_lower)

    positive_score = 0
    negative_score = 0

    negators = {"not", "no", "never"}
    previous_token = ""

    for token in tokens:
        is_negated = previous_token in negators
        if token in positive_words:
            if is_negated:
                negative_score += 1
            else:
                positive_score += 1
        elif token in negative_words:
            if is_negated:
                positive_score += 1
            else:
                negative_score += 1
        previous_token = token

    # Default to Negative on tie to avoid Neutral; adjust as needed
    sentiment = "Positive" if positive_score > negative_score else "Negative"
    print(f"Sentiment: {sentiment}")


if __name__ == "__main__":
    analyze_review_sentiment()

