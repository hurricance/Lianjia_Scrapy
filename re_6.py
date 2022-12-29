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

plt.figure(figsize=(25, 5))

for index, row in df_bj.iterrows():
    s = row['房子朝向'].split()[0]
    num = row['月租'] / row['面积']
    if s not in bj_dic.keys():
        bj_dic[s] = []
        bj_dic[s].append(num)
    else:
        bj_dic[s].append(num)
for key, val in bj_dic.items():
    bj_dic[key] = np.mean(bj_dic[key])
x = list(bj_dic.keys())
y = list(bj_dic.values())
for a,b,i in zip(x, y, range(len(x))):
    plt.text(a, b, '%.2f'%y[i], ha = 'center', va = 'bottom')
plt.bar(x, y, width = 0.5)
plt.title('北京各朝向平均单位面积租金(元)')
plt.subplot(1,5,1)

for index, row in df_sh.iterrows():
    s = row['房子朝向'].split()[0]
    num = row['月租'] / row['面积']
    if s not in sh_dic.keys():
        sh_dic[s] = []
        sh_dic[s].append(num)
    else:
        sh_dic[s].append(num)
for key, val in sh_dic.items():
    sh_dic[key] = np.mean(sh_dic[key])
x = list(sh_dic.keys())
y = list(sh_dic.values())
for a,b,i in zip(x, y, range(len(x))):
    plt.text(a, b, '%.2f'%y[i], ha = 'center', va = 'bottom')
plt.bar(x, y, width = 0.5)
plt.title('上海各朝向平均单位面积租金(元)')
plt.subplot(1,5,2)

for index, row in df_gz.iterrows():
    s = row['房子朝向'].split()[0]
    num = row['月租'] / row['面积']
    if s not in gz_dic.keys():
        gz_dic[s] = []
        gz_dic[s].append(num)
    else:
        gz_dic[s].append(num)
for key, val in gz_dic.items():
    gz_dic[key] = np.mean(gz_dic[key])
x = list(gz_dic.keys())
y = list(gz_dic.values())
for a,b,i in zip(x, y, range(len(x))):
    plt.text(a, b, '%.2f'%y[i], ha = 'center', va = 'bottom')
plt.bar(x, y, width = 0.5)
plt.title('广州各朝向平均单位面积租金(元)')
plt.subplot(1,5,3)

for index, row in df_sz.iterrows():
    s = row['房子朝向'].split()[0]
    num = row['月租'] / row['面积']
    if s not in sz_dic.keys():
        sz_dic[s] = []
        sz_dic[s].append(num)
    else:
        sz_dic[s].append(num)
for key, val in sz_dic.items():
    sz_dic[key] = np.mean(sz_dic[key])
x = list(sz_dic.keys())
y = list(sz_dic.values())
for a,b,i in zip(x, y, range(len(x))):
    plt.text(a, b, '%.2f'%y[i], ha = 'center', va = 'bottom')
plt.bar(x, y, width = 0.5)
plt.title('深圳各朝向平均单位面积租金(元)')
plt.subplot(1,5,4)

for index, row in df_gl.iterrows():
    s = row['房子朝向'].split()[0]
    num = row['月租'] / row['面积']
    if s not in gl_dic.keys():
        gl_dic[s] = []
        gl_dic[s].append(num)
    else:
        gl_dic[s].append(num)
for key, val in gl_dic.items():
    gl_dic[key] = np.mean(gl_dic[key])
x = list(gl_dic.keys())
y = list(gl_dic.values())
for a,b,i in zip(x, y, range(len(x))):
    plt.text(a, b, '%.2f'%y[i], ha = 'center', va = 'bottom')
plt.bar(x, y, width = 0.5)
plt.title('桂林各朝向平均单位面积租金(元)')
plt.subplot(1,5,5)

x = list(bj_dic.keys())
y = list(bj_dic.values())
for a,b,i in zip(x, y, range(len(x))):
    plt.text(a, b, '%.2f'%y[i], ha = 'center', va = 'bottom')
plt.bar(x, y, width = 0.5)
plt.title('北京各朝向平均单位面积租金(元)')
plt.subplot(1,5,1)

plt.show()
