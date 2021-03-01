from newsapi import NewsApiClient
from newspaper import Article

def getArticles(keywords):

    newsapi = NewsApiClient(api_key = "02cb3588872146ca9bcfaf6e2018fe2c")
    srcs = ["reuters", "bloomberg", "cnn"]
    dmns = ["https://www.reuters.com", "https://www.bloomberg.com", "https://edition.cnn.com/"]

    all_articles = []
    for i in range(0,3):
        articles = newsapi.get_everything(q = keywords, 
                                          sources = srcs[i],
                                          domains = dmns[i],
                                          from_param = "2021-01-28",
                                          to = "2021-02-27",
                                          language = "en",
                                          sort_by = "relevancy",
                                          page = 1)
                                        
        
        a = articles["articles"][0]
        article = {}
        article["source"] = a["source"]["id"]
        article["title"] = a["title"]
        article["url"] = a["url"]
        body = Article(a["url"])
        body.download()
        body.parse()
        article["text"] = body.text
        all_articles.append(article)

    return (all_articles)