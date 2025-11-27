
import requests
import matplotlib.pyplot as plt
import re
import spacy
import ginza

from bs4 import BeautifulSoup
from wordcloud import WordCloud

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
noun_list = []
for token in doc:
    if token.pos_ == "NOUN":
        print(token.text)
        noun_list.append(token.text)

noun_text = " ".join(noun_list)

font_path_gothic = '/usr/share/fonts/opentype/ipafontgothic/ipagp.ttf'

wc_noun = WordCloud(width=640, height=480, font_path=font_path_gothic, background_color="white", colormap='Blues').generate(noun_text)

plt.figure(figsize=(14,12))
plt.subplot(1, 2, 1)
plt.imshow(wc_noun)
plt.axis('off')
plt.title("名詞 WordCloud")
plt.show()
