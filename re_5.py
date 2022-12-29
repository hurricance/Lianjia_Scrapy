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

bj_dic = {}
sh_dic = {}
gz_dic = {}
sz_dic = {}
gl_dic = {}

for index, rows in df_bj.iterrows():
    s = rows['板块名称']
    num = rows['月租']
    if s not in bj_dic.keys():
        bj_dic[s] = []
        bj_dic[s].append(num)
    else:
        bj_dic[s].append(num)
for key, val in bj_dic.items():
    bj_dic[key] = np.mean(bj_dic[key])

for index, rows in df_sh.iterrows():
    s = rows['板块名称']
    num = rows['月租']
    if s not in sh_dic.keys():
        sh_dic[s] = []
        sh_dic[s].append(num)
    else:
        sh_dic[s].append(num)
for key, val in sh_dic.items():
    sh_dic[key] = np.mean(sh_dic[key])

for index, rows in df_gz.iterrows():
    s = rows['板块名称']
    num = rows['月租']
    if s not in gz_dic.keys():
        gz_dic[s] = []
        gz_dic[s].append(num)
    else:
        gz_dic[s].append(num)
for key, val in gz_dic.items():
    gz_dic[key] = np.mean(gz_dic[key])

for index, rows in df_sz.iterrows():
    s = rows['板块名称']
    num = rows['月租']
    if s not in sz_dic.keys():
        sz_dic[s] = []
        sz_dic[s].append(num)
    else:
        sz_dic[s].append(num)
for key, val in sz_dic.items():
    sz_dic[key] = np.mean(sz_dic[key])

for index, rows in df_gl.iterrows():
    s = rows['板块名称']
    num = rows['月租']
    if s not in gl_dic.keys():
        gl_dic[s] = []
        gl_dic[s].append(num)
    else:
        gl_dic[s].append(num)
for key, val in gl_dic.items():
    gl_dic[key] = np.mean(gl_dic[key])

bj_module = list(bj_dic.keys())
bj_average_rent = list(bj_dic.values())
length = len(bj_average_rent)
plt.figure(figsize=(15, 60)) #长宽比例
plt.hlines(y=range(length), xmin=0, xmax=bj_average_rent, color='pink') #绘制水平线
plt.plot(bj_average_rent, range(length), 'o') # 绘制端点
plt.yticks(range(length), bj_module) # 写出板块名称
plt.savefig('./要求5/1.png', dpi = 500) # 输出图像

sh_module = list(sh_dic.keys())
sh_average_rent = list(sh_dic.values())
length = len(sh_average_rent)
plt.figure(figsize=(15, 60))
plt.hlines(y=range(length), xmin=0, xmax=sh_average_rent, color='pink')
plt.plot(sh_average_rent, range(length), 'o')
plt.yticks(range(length), sh_module)
plt.savefig('./要求5/2.png', dpi = 500)

gz_module = list(gz_dic.keys())
gz_average_rent = list(gz_dic.values())
length = len(gz_average_rent)
plt.figure(figsize=(15, 60))
plt.hlines(y=range(length), xmin=0, xmax=gz_average_rent, color='pink')
plt.plot(gz_average_rent, range(length), 'o')
plt.yticks(range(length), gz_module)
plt.savefig('./要求5/3.png', dpi = 500)

sz_module = list(sz_dic.keys())
sz_average_rent = list(sz_dic.values())
length = len(sz_average_rent)
plt.figure(figsize=(15, 60))
plt.hlines(y=range(length), xmin=0, xmax=sz_average_rent, color='pink')
plt.plot(sz_average_rent, range(length), 'o')
plt.yticks(range(length), sz_module)
plt.savefig('./要求5/4.png', dpi = 500)

gl_module = list(gl_dic.keys())
gl_average_rent = list(gl_dic.values())
length = len(gl_average_rent)
plt.figure(figsize=(5, 4))
plt.hlines(y=range(length), xmin=0, xmax=gl_average_rent, color='pink')
plt.plot(gl_average_rent, range(length), 'o')
plt.yticks(range(length), gl_module)
plt.savefig('./要求5/5.png', dpi = 500)
