import jieba # 中文分词组件
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#步骤一：将文本导入到程序中
text=open(r'C:\Users\LIANG\Desktop\18河南计算机老乡群.txt',encoding='utf-8')

# 步骤二：净化文本数据
text_clean = open(r'C:\Users\LIANG\Desktop\text_clean.txt','w',encoding="utf-8-sig")
str_s=text.readlines()
for str in str_s:
    if str.find('[表情]')!=-1:
        str=str.replace('[表情]','')
    if str.find('你们')!=-1:
        str=str.replace('你们','')
    if str.find('我们') != -1:
        str = str.replace('我们', '')
    if str.find('不是') != -1:
        str = str.replace('不是', '')
    if str.find('可以') != -1:
        str = str.replace('可以', '')
    if str.find('李家') != -1:
        str = str.replace('李家', '')
    if str.find('2019')!=-1 or str.find('2020')!=-1 or str.find('2018')!=-1 or str.find('@')!=-1 or str=='' or str.find('[图片]')!=-1:
        continue
    else:
        text_clean.write(str)

#步骤四：利用jieba模块对聊天记录精确分词
text_clean = open(r'C:\Users\LIANG\Desktop\text_clean.txt','r',encoding="utf-8-sig").read()
text_jieba = jieba.cut(text_clean, cut_all=False)
text_split = " ".join(text_jieba)
print(text_split)


#步骤五：设置背景图 和字体
cloud_mask = np.array(Image.open(r'C:\Users\LIANG\Desktop\云朵.jpg'))
font = r'C:\Windows\Fonts\msyh.ttc'


#步骤六：生成词云
'''
scale : 			按比例放大画布 
background_color :	背景颜色
font_path :			字体
width :				宽
height :			高	
mask : 				nd-array or None类型 通常用于添加图片背景
max_words : 		要显示的词的最大个数
更多参数可以去看官方文档
'''
wordcloud = WordCloud( scale=10,background_color='white',width=200,height=200, font_path=font,mask=cloud_mask,max_words=300).generate(text_split)
#interpolation='bilinear',排线方式
plt.imshow(wordcloud,interpolation='bilinear')
#取消显示轴线
plt.axis('off')
#显示图片
plt.show()