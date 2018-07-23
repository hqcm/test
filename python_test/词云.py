import jieba
import jieba.analyse
import matplotlib.pyplot as plt
from wordcloud import WordCloud

with open (r'C:\Users\Administrator\Desktop\word_cloud-master\examples\a_new_hope.txt','r',encoding='UTF-8') as f:
    content=f.read()
#keywords = jieba.analyse.extract_tags(sentence, topK=20, withWeight=True, allowPOS=('n','nr','ns'))
wordcloud = WordCloud(background_color="white",width=1000, height=860, margin=2).generate(content)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()