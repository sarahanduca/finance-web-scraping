from get_dynamic_data import get_news_list
import pandas as pd
import sys

stock_code = sys.argv[1]
news_list = get_news_list(stock_code)

df = pd.DataFrame(news_list)
df.to_csv(f"news_{stock_code}.csv", index=False)
