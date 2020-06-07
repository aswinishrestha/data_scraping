import time
import requests
from bs4 import BeautifulSoup
import pprint

a = time.localtime()
today_date = str(a.tm_mday) + ", " + str(a.tm_year)


res = requests.get("https://www.sharesansar.com/category/latest?page=1")
soup = BeautifulSoup(res.text, "html.parser")
links = soup.select("[title]")
new_link = []
for i in links:
    if "class=\"featured-news-title\"" in str(i):
        new_link.append(i)
    else:
        pass
story = soup.select(".featured-news-title")
date = soup.select(".text-org")


def create_custom_dic(links, story, dates):
    count = 0
    combined_list = []
    links_list = []
    title_list = []
    for idx1, item2 in enumerate(links):
        href = links[idx1].get("href", None)
        article_date = dates[idx1].getText()[13:]
        if str(article_date) == today_date:
            links_list.append(href)
            count += 1

    for idx2, item2 in enumerate(story):
        title = story[idx2].getText()
        title_list.append(title)

    for j in range(count):
        combined_list.append({"Title": title_list[j], "Links": links_list[j]})

    return combined_list


pprint.pprint(create_custom_dic(new_link, story, date))