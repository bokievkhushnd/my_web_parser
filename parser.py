"""Parser for parsing a webpage and getting needed informarion"""


import json
import requests
from bs4 import BeautifulSoup as BS

URL = "https://habr.com/en/hub/programming/"

HABR_HTML_CODE = requests.get(URL).text
with open("/home/lashak/Desktop/appache2/habr_html_code.html", "w") as code:
    code.write(HABR_HTML_CODE)

SOUP = BS(HABR_HTML_CODE, 'html.parser')
TITLES = SOUP.find_all("h2", class_="post__title")
AUTHORS = SOUP.find_all(
    "span", class_="user-info__nickname user-info__nickname_small")
TIME_POSTED = SOUP.find_all("span", class_="post__time")
VIEWS = SOUP.find_all("span", class_="post-stats__views-count")
RELATEDS = SOUP.find_all('ul', class_="post__hubs inline-list")


ARTICLE_LIST = []
ARTICLE_NUM = 0
TITLE = [i.text.strip('\n') for i in TITLES]
AUTHOR = [i.text for i in AUTHORS]
LINK = [i.a["href"] for i in TITLES]
TIMES = [i.text for i in TIME_POSTED]
VIEW = [i.text for i in VIEWS]
RELATED = [[j.strip(" ,\n ") for j in i.text.split("\n\n")] for i in RELATEDS]

ARTICLE_LIST = []
ARTICLE_L = []
ARTICLE_NUM = 0
for i in range(len(VIEW)):
    articles = dict()
    article_dict = dict()
    article_dict["title"] = TITLE[ARTICLE_NUM]
    article_dict["author"] = AUTHOR[ARTICLE_NUM]
    article_dict["time posted"] = TIMES[ARTICLE_NUM]
    article_dict["related"] = RELATED[ARTICLE_NUM][1:-2]
    article_dict["link"] = LINK[ARTICLE_NUM]
    article_dict["views"] = VIEW[ARTICLE_NUM]
    ARTICLE_LIST.append(article_dict)
    ARTICLE_NUM += 1
    articles[f"Programming_post: #{ARTICLE_NUM}"] = article_dict
    ARTICLE_L.append(articles)
    with open("/home/lashak/Desktop/appache2/habr.json", "w") as article_json:
        json.dump(ARTICLE_L, article_json, indent=4, ensure_ascii=False)
