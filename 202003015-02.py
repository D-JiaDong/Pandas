#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
    wordcloud词云
'''
#下载 wordcloud模块 并导包
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
#步骤一：将文本导入到程序中
text=open(r'C:\Users\LIANG\Desktop\02.txt',encoding='utf-8')
text1 = open(r'C:\Users\LIANG\Desktop\ee.txt','w',encoding="utf-8-sig")
str0=text.readlines()
for str1 in str0:
    if str1.find('[表情]')!=-1:
        str1=str1.replace('[表情]','')
    if str1.find('哈') != -1:
        str1 = str1.replace('哈', '')
    if str1.find('2018')!=-1 or str1.find('2019')!=-1 or str1.find('2020')!=-1 or str1=='' or str1.find('[图片]')!=-1:
        continue
    else:
        # print(str1)
        text1.write(str1)
text2 = open(r'C:\Users\LIANG\Desktop\ee.txt','r',encoding="utf-8-sig").read()
word_jieba = jieba.cut(text2, cut_all=True)
word_split = " ".join(word_jieba)
#.generate(),根据哪个文本生成词云
#background_color背景颜色
#width,height:宽和高
#max_font_size,min_font_size最大最小字体的大小
#max_words:要显示多少词

# wordcloud = WordCloud(background_color='white',width=5000,height=5000,max_font_size=600,max_words=1000).generate(word_split)
#更改词云形状，导入其他图片
#PIL专门处理图像
from PIL import Image
import numpy as np
np.set_printoptions(threshold=np.inf)
alice_mask = np.array(Image.open(r'C:\Users\LIANG\Desktop\01.png'))
print(alice_mask.shape)
font = r'C:\Windows\Fonts\simkai.ttf'
wordcloud = WordCloud(background_color='white',width=5000,height=5000, font_path=font,mask=alice_mask,max_words=1000).generate(word_split)
#interpolation='bilinear',排线方式
plt.imshow(wordcloud,interpolation='bilinear')
#取消显示轴线
plt.axis('off')
plt.show()
