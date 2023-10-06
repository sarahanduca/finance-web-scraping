from get_dynamic_data import get_news_list
import pandas as pd
# from get_dynamic_data import get_news_data
import sys

stock_code = sys.argv[1]
news_list = get_news_list(stock_code = "ITUB4.SA")

df = pd.DataFrame(news_list)
df.to_csv(f"news_{stock_code}.csv", index=False)
