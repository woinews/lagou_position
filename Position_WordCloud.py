import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import pandas as pd
import os
import jieba.analyse

positiondata= pd.read_excel('positiondata.xlsx')
position_detail = positiondata['position_detail']

detail_list = []
for detail in position_detail:
    detail_list.append(str(detail).replace('\n' ,'').replace('\xa0',''))   #遍历获取position_detail列的文本并做处理
    
jieba.analyse.set_stop_words('delete_word.txt')     #这里首先要import jieba.analyse，且文本文件必须以utf-8格式保存，不然会出现编码错误
jieba.load_userdict('dict_world.txt')

keywords = jieba.analyse.extract_tags(str(detail_list), topK=100, withWeight=True, allowPOS=())

wc = WordCloud(background_color="white", max_words=200, 
               max_font_size=200, width=800, height=600, 
               font_path='C:\Windows\Fonts\SimHei.ttf')     #直接写字体名称，程序无法定位时可添加路径
#max_words是词云显示的最大词数，max_font_size是字体最大值

wc.generate_from_frequencies(dict(keywords))

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
