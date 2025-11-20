!pip install wordcloud
!pip install matplotlib
!apt -y install fonts-ipafont-gothic
!pip install Wikipedia

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import wikipedia

wikipedia.set_lang("ja")
try:
  page = wikipedia.page("神戸")
except wikipedia.exceptions.PageError:
    print("ページが見つかりませんでした。")
else:
  text = page.content

font_path_gothic = '/usr/share/fonts/opentype/ipafontgothic/ipagp.ttf'
wc=WordCloud(width=640,height=480, font_path=font_path_gothic)
wc.generate(text)

plt.figure(figsize=(12,10))
plt.imshow(wc)
plt.axis('off')
plt.show()
