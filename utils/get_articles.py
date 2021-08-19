from newsapi import NewsApiClient
from newspaper import Article

def getArticles(keywords, articles_per_source = 1):

    newsapi = NewsApiClient(api_key = '02cb3588872146ca9bcfaf6e2018fe2c')
    sources = ['reuters', 'bloomberg', 'cnn']
    domains = ['https://www.reuters.com', 'https://www.bloomberg.com', 'https://edition.cnn.com/']

    all_articles = []

    for source, domain in zip(sources, domains):

        articles = newsapi.get_everything(q = keywords, 
                                          sources = source,
                                          domains = domain,
                                          from_param = '2021-05-28',
                                          to = '2021-05-30',
                                          language = 'en',
                                          sort_by = 'relevancy',
                                          pageSize = articles_per_source,
                                          page = 1)
                                        
        for a in articles['articles']:

            body = Article(a['url'])
            body.download()
            body.parse()

            article = {}
            article['source'] = a['source']['name']
            article['title'] = a['title']
            article['url'] = a['url']
            article['text'] = body.text

            all_articles.append(article)

    return all_articles