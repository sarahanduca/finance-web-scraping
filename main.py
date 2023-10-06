from get_dynamic_data import get_news_list
import pandas as pd
import sys
from textblob import TextBlob

def sentiment_analyzer(text):
    blob = TextBlob(text)
    return blob.sentiment


stock_code = sys.argv[1]
news_list = get_news_list(stock_code)
for news in news_list:
    [polarity, subjectivity] = sentiment_analyzer(news["content"])
    news["polarity"] =  polarity
    news["subjectivity"] =  subjectivity

df = pd.DataFrame(news_list)
df.to_csv(f"news_{stock_code}.csv", index=False)
