import jieba

from wordcloud import WordCloud

with open('zyqnew.txt','r',encoding = 'UTF-8') as f:
    zyqnew_text = f.read()
cut_text = jieba.cut(zyqnew_text)

result = ' '.join(cut_text)



import matplotlib.pyplot as plt
wc = WordCloud(
    background_color = 'white',
    font_path = 'C:\\Windows\\Fonts\\STFANGSO.TTF',
    width = 500,
    height = 300,
    max_font_size = 50,
    min_font_size = 10,
)

wc.generate(result)
wc.to_file('w2.png')

plt.figure('jay')
plt.imshow(wc)
plt.axis('off')
plt.show()
