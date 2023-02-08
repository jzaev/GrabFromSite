import requests
from bs4 import BeautifulSoup

respond = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(respond.text, "html.parser")
title_rows = soup.findAll(name="span", class_="titleline")
score_rows = soup.findAll(name="td", class_="subtext")

titles_list = [title_rows[i].find(name="a").getText() for i in range(len(title_rows))]
href_list = [title_rows[i].find(name="a").get("href") for i in range(len(title_rows))]
score_list = [int(score_rows[i].find(name="span", class_="score").getText().split()[0]) for i in range(len(title_rows))]

print(titles_list)
print(href_list)
print(score_list)

best_position = score_list.index(max(score_list))

print('=================================================')

print(titles_list[best_position])
print(href_list[best_position])
print(score_list[best_position])
