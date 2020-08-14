import requests
import pandas as pd
from bs4 import BeautifulSoup
from IPython.display import display

url = "https://www.aclweb.org/anthology/events/acl-2020/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# my_dict = ["seq", "sub_seq", "conference", "year", "title", "author", "abstracts", "src", "# of sentence", "contents"]
#
# my_df = pd.DataFrame(data=[[4, 5], [6, 7]], index=range(0, 2), columns=['A', 'B'])
# display(pd.DataFrame(my_df))
#
# title_list = []
# author_list = []
# abstracts_list = []
# src_list = []
# contents = [[],[]]
# temp = 0
#
# my_titles = soup.select('#\32 020-acl-main > p:nth-child(3) > span > strong > a')
# my_authors = soup.select('p > span:nth-child(2) > a')
# abstracts = soup.findAll("div", {'class': 'card-body p-3 small'})

my_soup = soup.select('p > span:nth-child(2) > a')
print(my_soup)
print("=================================================================")

# for title in my_titles:
#     if temp == 0:
#         contents[0][0] = title.text
#         contents[0][1] = title.get('href')
#     else:
#         title_list.append(title.text)
#         src_list.append(title.get('href'))
#
# for author in my_authors:
#     author_list.append(author.text)

#
# for abstraction in abstracts:
#     abstracts_list.append(abstraction.text)
#
# print(len(title_list))
# 가장 긴 이름 찾기
# print(len(max(author_list, key=len)))
# print(min(title_list, key=len))
# print(len(abstracts_list))
# print(len(src_list))


# def Author():
#     p = soup.select('#main div')[2]
#     q = p.select("p span.d-block")
#
#     index2 = 0
#     index2_1 = 0
#
#     for i in q:
#         if index2 >= 1:
#             for j in i.select("a"):
#                 print(j.get_text())
#
#                 index2_1 += 1
#             index2_1 = 0
#             print("=========")
#
#         index2 += 1


# def Title():
#     number = soup.select('p > span:nth-child(2) > strong > a')
#
#     for j in range(len(number)):
#         p = soup.select('#main div')[j+1]
#         q = p.select("p span.d-block strong a")
#
#         index1 = 0
#         for i in q:
#             if index1 >= 1:
#                 print(i.get_text())
#
#             index1 += 1
#
#
# if __name__ == "__main__":
#     Title()



# contents = soup.select(
#     'p:nth-child(3) > span:nth-child(2) > strong > a'
# )


#


#
# for abstraction in abstracts:
#     print(abstraction.text)
#     print(abstraction.get('href'))


# print("title length : ", len(my_titles))
# print("author length : ", len(my_authors))
# print("abstraction length : ", len(abstracts))

# 참고 : https://beomi.github.io/gb-crawling/posts/2017-01-20-HowToMakeWebCrawler.html

