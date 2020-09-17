import re


def change_characters_tweet(tweet):
    """Change characters containing &."""
    tweet_no_character = tweet.replace('&amp;', '&')
    tweet_no_character = tweet_no_character.replace('&lt;', '<')
    tweet_no_character = tweet_no_character.replace('&gt;','>')
    return tweet_no_character


def remove_url(tweet):
    tweet_without_url = re.sub(r"http\S+", "", tweet)
    return tweet_without_url


def is_small_tweet(tweet):
    """Check if the tweet is small (Less than three words)"""
    tweet_words = len(re.findall(r'\w+', tweet))
    if tweet_words < 4:
        return True