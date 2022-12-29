import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

df_bj = pd.read_csv('./final_data/bj.csv')
df_sh = pd.read_csv('./final_data/sh.csv')
df_gz = pd.read_csv('./final_data/gz.csv')
df_sz = pd.read_csv('./final_data/sz.csv')
df_gl = pd.read_csv('./final_data/gl.csv')

bj_one_bedroom = []
bj_two_bedroom = []
bj_three_bedroom = []
sh_one_bedroom = []
sh_two_bedroom = []
sh_three_bedroom = []
gz_one_bedroom = []
gz_two_bedroom = []
gz_three_bedroom = []
sz_one_bedroom = []
sz_two_bedroom = []
sz_three_bedroom = []
gl_one_bedroom = []
gl_two_bedroom = []
gl_three_bedroom = []

for index, rows in df_bj.iterrows():
    temp = int(re.findall(r"\d+\.?\d*", rows['房型'])[0])
    if temp == 1:
        bj_one_bedroom.append(rows['月租'])
    elif temp == 2:
        bj_two_bedroom.append(rows['月租'])
    elif temp == 3:
        bj_three_bedroom.append(rows['月租'])

for index, rows in df_sh.iterrows():
    temp = int(re.findall(r"\d+\.?\d*", rows['房型'])[0])
    if temp == 1:
        sh_one_bedroom.append(rows['月租'])
    elif temp == 2:
        sh_two_bedroom.append(rows['月租'])
    elif temp == 3:
        sh_three_bedroom.append(rows['月租'])

for index, rows in df_gz.iterrows():
    temp = int(re.findall(r"\d+\.?\d*", rows['房型'])[0])
    if temp == 1:
        gz_one_bedroom.append(rows['月租'])
    elif temp == 2:
        gz_two_bedroom.append(rows['月租'])
    elif temp == 3:
        gz_three_bedroom.append(rows['月租'])

for index, rows in df_sz.iterrows():
    temp = int(re.findall(r"\d+\.?\d*", rows['房型'])[0])
    if temp == 1:
        sz_one_bedroom.append(rows['月租'])
    elif temp == 2:
        sz_two_bedroom.append(rows['月租'])
    elif temp == 3:
        sz_three_bedroom.append(rows['月租'])

for index, rows in df_gl.iterrows():
    temp = int(re.findall(r"\d+\.?\d*", rows['房型'])[0])
    if temp == 1:
        gl_one_bedroom.append(rows['月租'])
    elif temp == 2:
        gl_two_bedroom.append(rows['月租'])
    elif temp == 3:
        gl_three_bedroom.append(rows['月租'])

bj_one = [np.mean(bj_one_bedroom), max(bj_one_bedroom), min(bj_one_bedroom), np.median(bj_one_bedroom)]
sh_one = [np.mean(sh_one_bedroom), max(sh_one_bedroom), min(sh_one_bedroom), np.median(sh_one_bedroom)]
gz_one = [np.mean(gz_one_bedroom), max(gz_one_bedroom), min(gz_one_bedroom), np.median(gz_one_bedroom)]
sz_one = [np.mean(sz_one_bedroom), max(sz_one_bedroom), min(sz_one_bedroom), np.median(sz_one_bedroom)]
gl_one = [np.mean(gl_one_bedroom), max(gl_one_bedroom), min(gl_one_bedroom), np.median(gl_one_bedroom)]

bj_two = [np.mean(bj_two_bedroom), max(bj_two_bedroom), min(bj_two_bedroom), np.median(bj_two_bedroom)]
sh_two = [np.mean(sh_two_bedroom), max(sh_two_bedroom), min(sh_two_bedroom), np.median(sh_two_bedroom)]
gz_two = [np.mean(gz_two_bedroom), max(gz_two_bedroom), min(gz_two_bedroom), np.median(gz_two_bedroom)]
sz_two = [np.mean(sz_two_bedroom), max(sz_two_bedroom), min(sz_two_bedroom), np.median(sz_two_bedroom)]
gl_two = [np.mean(gl_two_bedroom), max(gl_two_bedroom), min(gl_two_bedroom), np.median(gl_two_bedroom)]

bj_three = [np.mean(bj_three_bedroom), max(bj_three_bedroom), min(bj_three_bedroom), np.median(bj_three_bedroom)]
sh_three = [np.mean(sh_three_bedroom), max(sh_three_bedroom), min(sh_three_bedroom), np.median(sh_three_bedroom)]
gz_three = [np.mean(gz_three_bedroom), max(gz_three_bedroom), min(gz_three_bedroom), np.median(gz_three_bedroom)]
sz_three = [np.mean(sz_three_bedroom), max(sz_three_bedroom), min(sz_three_bedroom), np.median(sz_three_bedroom)]
gl_three = [np.mean(gl_three_bedroom), max(gl_three_bedroom), min(gl_three_bedroom), np.median(gl_three_bedroom)]

x = np.array(["北京", "上海", "广州", "深圳", "桂林"])
y = np.array([bj_one[0], sh_one[0], gz_one[0], sz_one[0], gl_one[0]])
for a,b,i in zip(x,y,range(len(x))): # zip 函数
    plt.text(a, b, "%.2f"%y[i], ha = 'center', va = 'bottom') # plt.text 函数
plt.bar(x, y, width = 0.5)
plt.title('一居室平均月租金(元)')
plt.subplot(2,2,1)

x = np.array(["北京", "上海", "广州", "深圳", "桂林"])
y = np.array([bj_one[1], sh_one[1], gz_one[1], sz_one[1], gl_one[1]])
for a,b,i in zip(x,y,range(len(x))): # zip 函数
    plt.text(a, b, y[i], ha = 'center', va = 'bottom') # plt.text 函数
plt.bar(x, y, width = 0.5)
plt.title('一居室最高月租金(元)')
plt.subplot(2,2,2)

x = np.array(["北京", "上海", "广州", "深圳", "桂林"])
y = np.array([bj_one[2], sh_one[2], gz_one[2], sz_one[2], gl_one[2]])
for a,b,i in zip(x,y,range(len(x))): # zip 函数
    plt.text(a, b, y[i], ha = 'center', va = 'bottom') # plt.text 函数
plt.bar(x, y, width = 0.5)
plt.title('一居室最低月租金(元)')
plt.subplot(2,2,3)

x = np.array(["北京", "上海", "广州", "深圳", "桂林"])
y = np.array([bj_one[3], sh_one[3], gz_one[3], sz_one[3], gl_one[3]])
for a,b,i in zip(x,y,range(len(x))): # zip 函数
    plt.text(a, b, y[i], ha = 'center', va = 'bottom') # plt.text 函数
plt.bar(x, y, width = 0.5)
plt.title('一居室月租金中位数(元)')
plt.subplot(2,2,4)

x = np.array(["北京", "上海", "广州", "深圳", "桂林"])
y = np.array([bj_one[0], sh_one[0], gz_one[0], sz_one[0], gl_one[0]])
for a,b,i in zip(x,y,range(len(x))): # zip 函数
    plt.text(a, b, "%.2f"%y[i], ha = 'center', va = 'bottom') # plt.text 函数
plt.bar(x, y, width = 0.5)
plt.title('一居室平均月租金(元)')
plt.subplot(2,2,1)

plt.show()

x = np.array(["北京", "上海", "广州", "深圳", "桂林"])
y = np.array([bj_two[0], sh_two[0], gz_two[0], sz_two[0], gl_two[0]])
for a,b,i in zip(x,y,range(len(x))): # zip 函数
    plt.text(a, b, "%.2f"%y[i], ha = 'center', va = 'bottom') # plt.text 函数
plt.bar(x, y, width = 0.5)
plt.title('二居室平均月租金(元)')
plt.subplot(2,2,1)

x = np.array(["北京", "上海", "广州", "深圳", "桂林"])
y = np.array([bj_two[1], sh_two[1], gz_two[1], sz_two[1], gl_two[1]])
for a,b,i in zip(x,y,range(len(x))): # zip 函数
    plt.text(a, b, y[i], ha = 'center', va = 'bottom') # plt.text 函数
plt.bar(x, y, width = 0.5)
plt.title('二居室最高月租金(元)')
plt.subplot(2,2,2)

x = np.array(["北京", "上海", "广州", "深圳", "桂林"])
y = np.array([bj_two[2], sh_two[2], gz_two[2], sz_two[2], gl_two[2]])
for a,b,i in zip(x,y,range(len(x))): # zip 函数
    plt.text(a, b, y[i], ha = 'center', va = 'bottom') # plt.text 函数
plt.bar(x, y, width = 0.5)
plt.title('二居室最低月租金(元)')
plt.subplot(2,2,3)

x = np.array(["北京", "上海", "广州", "深圳", "桂林"])
y = np.array([bj_two[3], sh_two[3], gz_two[3], sz_two[3], gl_two[3]])
for a,b,i in zip(x,y,range(len(x))): # zip 函数
    plt.text(a, b, y[i], ha = 'center', va = 'bottom') # plt.text 函数
plt.bar(x, y, width = 0.5)
plt.title('二居室月租金中位数(元)')
plt.subplot(2,2,4)

x = np.array(["北京", "上海", "广州", "深圳", "桂林"])
y = np.array([bj_two[0], sh_two[0], gz_two[0], sz_two[0], gl_two[0]])
for a,b,i in zip(x,y,range(len(x))): # zip 函数
    plt.text(a, b, "%.2f"%y[i], ha = 'center', va = 'bottom') # plt.text 函数
plt.bar(x, y, width = 0.5)
plt.title('二居室平均月租金(元)')
plt.subplot(2,2,1)

plt.show()

x = np.array(["北京", "上海", "广州", "深圳", "桂林"])
y = np.array([bj_three[0], sh_three[0], gz_three[0], sz_three[0], gl_three[0]])
for a,b,i in zip(x,y,range(len(x))): # zip 函数
    plt.text(a, b, "%.2f"%y[i], ha = 'center', va = 'bottom') # plt.text 函数
plt.bar(x, y, width = 0.5)
plt.title('三居室平均月租金(元)')
plt.subplot(2,2,1)

x = np.array(["北京", "上海", "广州", "深圳", "桂林"])
y = np.array([bj_three[1], sh_three[1], gz_three[1], sz_three[1], gl_three[1]])
for a,b,i in zip(x,y,range(len(x))): # zip 函数
    plt.text(a, b, y[i], ha = 'center', va = 'bottom') # plt.text 函数
plt.bar(x, y, width = 0.5)
plt.title('三居室最高月租金(元)')
plt.subplot(2,2,2)

x = np.array(["北京", "上海", "广州", "深圳", "桂林"])
y = np.array([bj_three[2], sh_three[2], gz_three[2], sz_three[2], gl_three[2]])
for a,b,i in zip(x,y,range(len(x))): # zip 函数
    plt.text(a, b, y[i], ha = 'center', va = 'bottom') # plt.text 函数
plt.bar(x, y, width = 0.5)
plt.title('三居室最低月租金(元)')
plt.subplot(2,2,3)

x = np.array(["北京", "上海", "广州", "深圳", "桂林"])
y = np.array([bj_three[3], sh_three[3], gz_three[3], sz_three[3], gl_three[3]])
for a,b,i in zip(x,y,range(len(x))): # zip 函数
    plt.text(a, b, y[i], ha = 'center', va = 'bottom') # plt.text 函数
plt.bar(x, y, width = 0.5)
plt.title('三居室月租金中位数(元)')
plt.subplot(2,2,4)

x = np.array(["北京", "上海", "广州", "深圳", "桂林"])
y = np.array([bj_three[0], sh_three[0], gz_three[0], sz_three[0], gl_three[0]])
for a,b,i in zip(x,y,range(len(x))): # zip 函数
    plt.text(a, b, "%.2f"%y[i], ha = 'center', va = 'bottom') # plt.text 函数
plt.bar(x, y, width = 0.5)
plt.title('三居室平均月租金(元)')
plt.subplot(2,2,1)

plt.show()
# x=np.arange(4)#柱状图在横坐标上的位置
# #列出你要显示的数据，数据的列表长度与x长度相同
# y1=[bj_one[0], bj_one[1], bj_one[2], bj_one[3]]
# y2=[sh_one[0], sh_one[1], sh_one[2], sh_one[3]]
# y3=[gz_one[0], gz_one[1], gz_one[2], gz_one[3]]
# y4=[sz_one[0], sz_one[1], sz_one[2], sz_one[3]]
# y5=[gl_one[0], gl_one[1], gl_one[2], gl_one[3]]

# bar_width=0.1#设置柱状图的宽度
# tick_label = ['均价','最高价','最低价','中位数']

# #绘制并列柱状图
# plt.bar(x,y1,bar_width,color='red',label='北京')
# plt.bar(x+bar_width,y2,bar_width,color='blue',label='上海')
# plt.bar(x+bar_width*2,y3,bar_width,color='green',label='广州')
# plt.bar(x+bar_width*3,y4,bar_width,color='brown',label='深圳')
# plt.bar(x+bar_width*4,y5,bar_width,color='orange',label='桂林')

# plt.legend()#显示图例，即label
# plt.xticks(x+bar_width/2,tick_label)#显示x坐标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
# plt.show()