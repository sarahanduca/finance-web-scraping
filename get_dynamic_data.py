from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

URL = "https://finance.yahoo.com/"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)

def get_news_list(stock_code):    
    news_list_url = f"{URL}quote/{stock_code}?p={stock_code}"
    driver.get(news_list_url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    news_list = soup.find_all("li", class_="js-stream-content")
    news_results = []
    for news in news_list:
        div = news.find("div")
        if(div.has_attr("data-test-locator") and div["data-test-locator"] == "mega"):
            link = news.select_one("div > div > div > h3 > a")
            news_url = f"{URL}{link['href']}"
            driver.get(news_url)
            time.sleep(5)
            news_soup = BeautifulSoup(driver.page_source, "html.parser")
            paragraphs = news_soup.find("div", attrs={"class":"caas-body"})
            news_results.append(
                {
                    "link": link["href"] if link else None,
                    "title": news.find("h3").get_text(),
                    "content": "\n".join([p.get_text() for p in paragraphs.find_all("p")]) if paragraphs else None,
                    "date": news_soup.find("time")["datetime"]
                }
            )
    driver.quit()
    return news_results


