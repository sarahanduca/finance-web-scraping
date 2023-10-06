from get_dynamic_data import get_news_list
# from get_dynamic_data import get_news_data
import sys

stock_code = sys.argv[1]
news_list = get_news_list(stock_code = "ITUB4.SA")

f = open("ITAU.txt", "a")
for news in news_list:
    f.write(news["title"])
    f.write("\n")
    f.write(news["content"])
    f.write("\n")
    f.write(news["date"])   
    f.write("\n")
f.close()

