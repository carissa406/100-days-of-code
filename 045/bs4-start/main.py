# from bs4 import BeautifulSoup
# #import lxml
# import requests

# response = requests.get("https://news.ycombinator.com/")
# yc_webpage = response.text
# soup = BeautifulSoup(yc_webpage, "html.parser")

# articles = soup.find_all(name='span', class_='titleline')
# # article_text = article_tag.getText()
# # article_link = article_tag.find(name="a").get("href")

# article_text = []
# article_links = []
# for article_tag in articles:
#     #print(article_tag)
#     print(article_tag.getText())
#     #article_text.append(article_tag.getText())
#     #article_links.append(article_tag.find(name="a").get("href"))

# article_upvotes = soup.find_all(name='span',class_='score').getText()

# print(article_text)
# print(article_links)
# print(article_upvotes)

from bs4 import BeautifulSoup
import requests
 
 
response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
 
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
 
article_texts = []
article_links = []
 
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find(name="a").get("href")
    article_links.append(link)
 
upvote_rows = soup.find_all(name="td", class_="subtext")
article_upvotes = [int(upvote.getText().split()[0]) for upvote in soup.find_all(name="span", class_="score")]
 
#print(article_texts[article_upvotes.index(max(article_upvotes))])
#print(article_links[article_upvotes.index(max(article_upvotes))])
print(article_texts)
print(article_links)
print(article_upvotes)



































# all_titles = soup.find_all(name="span", class_ = "titleline")
# for titles in all_titles:
#     print(titles.getText())


# with open("Day 45/bs4-start/website.html", encoding="utf-8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser') #'lxml'
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a) #anchor tags
# print(soup.li) #list

# print(soup.find_all(name="a")) #print all anchors in a list

# #get all the anchor tags
# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     #gets just the text
#     print(tag.getText())
#     #gets just the links
#     print(tag.get("href"))

# #finding a specific one using ids
# heading = soup.find(name="h1", id="name")
# print(heading)

# #find a specific item using class
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))

# #select(gets all) select one (gets the first match), anchor inside a paragraph 
# company_url = soup.select_one(selector="p a")
# print(company_url)
# #by ids
# company_url = soup.select_one(selector="#name")
# print(company_url)
# #by class, selecting all
# headings = soup.select(".heading")
# print(headings)