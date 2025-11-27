
import requests
from bs4 import BeautifulSoup
import re
import spacy
import ginza

url = "https://www.yahoo.co.jp/"
req = requests.get(url)
contents = BeautifulSoup(req.content, "html.parser")
data_list = contents.find_all(href=re.compile("news.yahoo.co.jp/pickup"))

text1 = ""
for data in data_list:
  text1 += data.text + "\n"

print("=== 取得したニュースタイトル ===")
print(text1)

nlp = spacy.load("ja_ginza")
doc = nlp(text1)

print("=== 名詞のみ ===")
for token in doc:
    if token.pos_ == "NOUN":
        print(token.text)
