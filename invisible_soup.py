from bs4 import BeautifulSoup
import requests
import random

fo = open("invisible_template.html", "r")
html_template = fo.read();
fo.close()

unincorporated = requests.get("http://la.lawsoup.org/law-basics/list-of-unincorporated-communities-of-los-angeles-county/")

html_doc = unincorporated.text

soup = BeautifulSoup(html_doc, "html.parser")

city_list = soup.find_all("p")

del city_list[:2]
del city_list[-2:]

city_set = []

for city in city_list:
	city_name = city.text
	city_set.append(city_name)

# print city_set

invisible = requests.get("http://www.ruanyifeng.com/calvino/2007/01/cities_seven.html")

html_doc = invisible.text

soup = BeautifulSoup(html_doc, "html.parser")

paras = soup.find("div", class_="entry-body")

paras = paras.find_all("p")

para_set = []
p_set = []

for para in paras:
	content = para.text
	content = content.replace("Moriana", "{0}").replace("Clarice", "{0}").replace("Eusapia", "{0}").replace("Beersheba", "{0}").replace("Leonia", "{0}")
	para_set.append(content)

del para_set[:7]
del para_set[-12:]

for p in para_set:
	p = p.format(random.choice(city_set))
	p_set.append(p)

title_set = []

heads = soup.find("div", class_="entry-body")

heads = heads.find_all("h3")

for head in heads:
	title = head.text
	title = title.replace(" 5.", "").replace(" 4.", "").replace(" 3.", "").replace(" 2.", "").replace(" 1.", "").lower()
	title_set.append(title)

ghost = requests.get("http://www.bldgblog.com/2015/12/ghost-streets-of-los-angeles/")

html_doc = ghost.text

soup = BeautifulSoup(html_doc, "html.parser")

main = soup.find("div", class_= "entry-content")

image = main.img["src"]

html_file = html_template.format(random.choice(p_set), image, random.choice(title_set))

fo = open("invisible_cities.html", "w")
fo.write(html_file);
fo.close()