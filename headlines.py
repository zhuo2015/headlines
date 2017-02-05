# coding:utf-8
# copyright: freedom

from flask import Flask
import feedparser


app = Flask(__name__)

pubs = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
        'smzdm': 'http://post.smzdm.com/feed'}


@app.route('/')
@app.route('/<puburl>')      # <xx>, receive a args as variable
def get_news(puburl='smzdm'):
    feed = feedparser.parse(pubs[puburl])
    first_article = feed['entries'][0]
    return """<html>
                <body>
                    <h1> BBC Headlines </h1>
                    <b>{0}</b> <br/>
                    <i>{1}</i> <br/>
                    <p>{2}</p> <br/>
                </body>
                </html>""".format(first_article.get("title"), first_article.
                    get("published"), first_article.get("summary"))

if __name__ == "__main__":
    app.run()