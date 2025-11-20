
!pip install wordcloud
!pip install matplotlib
!apt -y install fonts-ipafont-gothic
!pip install Wikipedia
!pip install spacy
!pip install ginza ja-ginza

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import wikipedia
import spacy
import ginza
import pandas as pd

nlp = spacy.load("ja_ginza")

wikipedia.set_lang("ja")
try:
  page = wikipedia.page("神戸")
except wikipedia.exceptions.PageError:
    print("ページが見つかりませんでした。")
else:
  text = page.content

# 形態素解析
m = nlp(text)

# DataFrame作成
result_list = []
for sent in m.sents:
  for token in sent:
    output_string = f"{token.i} {token.orth_} {token.lemma_} {token.pos_} {token.tag_} {token.dep_} {token.head.i}¥n"
    result_list.append([token.orth_, token.lemma_, token.pos_, token.tag_])

# 名詞と形容詞を抽出
df = pd.DataFrame(result_list, columns = ['text', 'lemma', 'pos','tag'])
font_path_gothic = '/usr/share/fonts/opentype/ipafontgothic/ipagp.ttf'
noun_text = ' '.join(df[df['tag'].str.startswith('名詞')]['text'].to_list())
adj_text  = ' '.join(df[df['tag'].str.startswith('形容詞')]['text'].to_list())


wc_noun = WordCloud(width=640, height=480, font_path=font_path_gothic, background_color="white", colormap='Blues').generate(noun_text)

wc_adj = WordCloud(width=640, height=480, font_path=font_path_gothic, background_color="white", colormap='Reds').generate(adj_text)


# 表示
plt.figure(figsize=(14,12))

plt.subplot(1, 2, 1)
plt.imshow(wc_noun)
plt.axis('off')
plt.title("名詞 WordCloud")

plt.subplot(1, 2, 2)
plt.imshow(wc_adj)
plt.axis('off')
plt.title("形容詞 WordCloud")

plt.show()
