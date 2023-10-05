from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def get_dynamic_data(stock_code):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    url = f"https://finance.yahoo.com/quote/{stock_code}?p={stock_code}"
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    news_list = soup.find_all("li", class_="js-stream-content")
    news_results = []
    for news in news_list:
        div = news.find("div")
        if(div.has_attr("data-test-locator") and div["data-test-locator"] == "mega"):
            link = news.select_one("div > div > div > h3 > a")
            news_results.append(
                {
                    "link": link["href"] if link else None,
                    "title": news.find("h3").get_text(),
                }
            )
    driver.quit()
    return news_results