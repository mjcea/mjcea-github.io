import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.tibia.com/news/?subtopic=latestnews'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('div', id='News')
    news_data = []

    for article in articles:
            news_dates = article.find_all('div', class_='NewsHeadlineDate')
            news_titles = article.find_all('div', class_='NewsHeadlineText')
            news_texts = article.find_all('td', class_='NewsTableContainer')

            for news_date in news_dates:
                for news_title in news_titles:
                    for news_text in news_texts:
                        news_item = {
                            'title': news_title.text.strip(),
                            'date': news_date.text.strip(),
                            'text': news_text.text.strip()
                        }
                        news_data.append(news_item)

    news_json = json.dumps(news_data,  indent = 1)
    #print(news_json)
    
    file_name = "noticias-tibia.json"
    with open(file_name, "w") as arquivo_json:
        json.dump(news_json, arquivo_json)
else:
    print("404")