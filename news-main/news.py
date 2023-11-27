import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.tibia.com/news/?subtopic=latestnews'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('div', id='News')
    news_data = []
    out_file = open("tibia-news.json", "w")
    
    for article in articles:
        news_dates = article.find_all('div', class_='NewsHeadlineDate')
        news_titles = article.find_all('div', class_='NewsHeadlineText')
        news_texts = article.find_all('table', class_='NewsTable')

        for i in range(len(news_texts)):
            news_item = {
                "date": news_dates[i].text,
                "title": news_titles[i].text,
                "text": str(news_texts[i])
            }
            news_data.append(news_item)

    news_json = json.dump(news_data, out_file, indent = 4)
else:
    print("404")