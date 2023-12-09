import requests
from bs4 import BeautifulSoup as bs

HOME_URL = 'https://news.am/'


class NewsLinkScraper:
    def __init__(self, url: str):
        self.url = url

    def scrapy_top_news_links(self):
        try:
            r = requests.get(self.url)
            r.raise_for_status()

            html = bs(r.content, 'html.parser')
            top_news = html.find('div', class_='top-news')

            if top_news:
                top_desk_active = top_news.find('div', class_='top-desk active')

                if top_desk_active:
                    news_items = top_desk_active.find_all('a', class_='news-item')[:5]
                    latest_news_links = []
                    for news_item in news_items:
                        href = news_item['href']
                        correct_href = self.url + href[5:]
                        latest_news_links.append(correct_href)

                    return latest_news_links

        except requests.RequestException as e:

            print(f"An error occurred: {e}")

        return None


class TopNewsScraper:
    @staticmethod
    def get_all_info(url):
        r = requests.get(url)
        if r.status_code == 200:
            html = bs(r.content, 'html.parser')
            section_article = html.find('section', class_='section-article')
            if section_article:
                article_title = section_article.find('div', class_='article-title')
                img_tag = section_article.find('div', class_="article-text").find('img')
                article_body_span = section_article.find('span', class_='article-body').findAll('p')
                article_texts = [article.get_text(strip=True) for article in article_body_span]

                return {
                    'article_title': article_title.text,
                    'image_url': HOME_URL + img_tag['src'],
                    'article_texts': article_texts
                }
        return None
