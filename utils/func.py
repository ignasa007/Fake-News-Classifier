from .retrieve_tweet_keywords import summarize
from .retrieve_tweet_text import getText
from .get_articles import getArticles
from .article_summariser import getSummary

def getArticles(url):

    tweet = getText(url)
    tweet_summary = summarize(tweet)
    all_articles = getArticles(tweet_summary)
    
    return tweet, all_articles