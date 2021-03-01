from retrieve_tweet_keywords import summarize
from retrieve_tweet_text import getText
from get_articles import getArticles
from article_summariser import getSummary

def getMatchingArticles(url):

    res = {}
    tweet_text = getText(url)
    tweet_summary = summarize(tweet_text)
    all_articles = getArticles(tweet_summary)

    for article in all_articles:
        article["summary"] = getSummary(article["text"])
        del article["text"]
    
    res["tweet_url"] = url
    res["tweet_summary"] = tweet_summary
    res["articles"] = all_articles
    
    return res