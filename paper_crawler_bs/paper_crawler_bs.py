import requests
from bs4 import BeautifulSoup

url = "https://www.aclweb.org/anthology/events/acl-2020/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

my_titles = soup.select(
    'p > span:nth-child(2) > strong > a'
    )

my_authors = soup.select(
    'p > span:nth-child(2) > a'
)

# for title in my_titles:
#     print(title.text)

for author in my_authors:
    print(author.text)

# 참고 : https://beomi.github.io/gb-crawling/posts/2017-01-20-HowToMakeWebCrawler.html
