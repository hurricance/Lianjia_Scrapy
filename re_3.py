import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

def average_rent(df_bj, df_sh, df_gz, df_sz, df_gl):
    bj_average_rent = df_bj['月租'].mean() # 由于获取平均数
    sh_average_rent = df_sh['月租'].mean()
    gz_average_rent = df_gz['月租'].mean()
    sz_average_rent = df_sz['月租'].mean()
    gl_average_rent = df_gl['月租'].mean()

    x = np.array(["北京租金均价", "上海租金均价", "广州租金均价", "深圳租金均价", "桂林租金均价"])
    y = np.array([bj_average_rent, sh_average_rent, gz_average_rent, sz_average_rent, gl_average_rent])

    for a,b,i in zip(x,y,range(len(x))): # zip函数由于生成元组
        plt.text(a, b, "%.2f"%y[i], ha = 'center', va = 'bottom') # 由于在条形图上方显示数值
    plt.bar(x, y, width = 0.5)
    plt.title('各地平均月租金(元)')
    plt.subplot(2, 2, 1) #子图

def max_rent(df_bj, df_sh, df_gz, df_sz, df_gl):
    bj_max_rent = df_bj['月租'].max()
    sh_max_rent = df_sh['月租'].max()
    gz_max_rent = df_gz['月租'].max()
    sz_max_rent = df_sz['月租'].max()
    gl_max_rent = df_gl['月租'].max()
    x = np.array(["北京租金最高价", "上海租金最高价", "广州租金最高价", "深圳租金最高价", "桂林租金最高价"])
    y = np.array([bj_max_rent, sh_max_rent, gz_max_rent, sz_max_rent, gl_max_rent])

    for a,b,i in zip(x, y, range(len(x))):
        plt.text(a, b, y[i], ha = 'center', va = 'bottom')
    plt.bar(x, y, width = 0.5)
    plt.title('各地最高月租金(元)')
    plt.subplot(2, 2, 2)

def min_rent(df_bj, df_sh, df_gz, df_sz, df_gl):
    bj_min_rent = df_bj['月租'].min()
    sh_min_rent = df_sh['月租'].min()
    gz_min_rent = df_gz['月租'].min()
    sz_min_rent = df_sz['月租'].min()
    gl_min_rent = df_gl['月租'].min()
    x = np.array(["北京租金最低价", "上海租金最低价", "广州租金最低价", "深圳租金最低价", "桂林租金最低价"])
    y = np.array([bj_min_rent, sh_min_rent, gz_min_rent, sz_min_rent, gl_min_rent])

    for a,b,i in zip(x, y, range(len(x))):
        plt.text(a, b, y[i], ha = 'center', va = 'bottom')
    plt.bar(x, y, width = 0.5)
    plt.title('各地最低月租金(元)')
    plt.subplot(2, 2, 3)

def median_rent(df_bj, df_sh, df_gz, df_sz, df_gl):
    bj_median_rent = df_bj['月租'].median()
    sh_median_rent = df_sh['月租'].median()
    gz_median_rent = df_gz['月租'].median()
    sz_median_rent = df_sz['月租'].median()
    gl_median_rent = df_gl['月租'].median()
    x = np.array(["北京租金中位数", "上海租金中位数", "广州租金中位数", "深圳租金中位数", "桂林租金中位数"])
    y = np.array([bj_median_rent, sh_median_rent, gz_median_rent, sz_median_rent, gl_median_rent])

    for a,b,i in zip(x, y, range(len(x))):
        plt.text(a, b, y[i], ha = 'center', va = 'bottom')
    plt.bar(x, y, width = 0.5)
    plt.title('各地月租金中位数(元)')
    plt.subplot(2, 2, 4)

def average_rent_per_unit(bj_rent_per_unit, sh_rent_per_unit, gz_rent_per_unit, sz_rent_per_unit, gl_rent_per_unit):
    bj_average_rent_per_unit = np.mean(bj_rent_per_unit)
    sh_average_rent_per_unit = np.mean(sh_rent_per_unit)
    gz_average_rent_per_unit = np.mean(gz_rent_per_unit)
    sz_average_rent_per_unit = np.mean(sz_rent_per_unit)
    gl_average_rent_per_unit = np.mean(gl_rent_per_unit)
    x = np.array(["北京单位面积租金", "上海单位面积租金", "广州单位面积租金", "深圳单位面积租金", "桂林单位面积租金"])
    y = np.array([bj_average_rent_per_unit, sh_average_rent_per_unit, gz_average_rent_per_unit, sz_average_rent_per_unit, gl_average_rent_per_unit])

    for a,b,i in zip(x, y, range(len(x))):
        plt.text(a, b, "%.2f"%y[i], ha = 'center', va = 'bottom')
    plt.bar(x, y, width = 0.5)
    plt.title('各地平均单位面积租金(元/平米)')
    plt.subplot(2, 2, 1)

def max_rent_per_unit(bj_rent_per_unit, sh_rent_per_unit, gz_rent_per_unit, sz_rent_per_unit, gl_rent_per_unit):
    bj_max_average_rent_per_unit = max(bj_rent_per_unit)
    sh_max_average_rent_per_unit = max(sh_rent_per_unit)
    gz_max_average_rent_per_unit = max(gz_rent_per_unit)
    sz_max_average_rent_per_unit = max(sz_rent_per_unit)
    gl_max_average_rent_per_unit = max(gl_rent_per_unit)
    x = np.array(["北京最高单位面积租金", "上海最高单位面积租金", "广州最高单位面积租金", "深圳最高单位面积租金", "桂林最高单位面积租金"])
    y = np.array([bj_max_average_rent_per_unit, sh_max_average_rent_per_unit, gz_max_average_rent_per_unit, sz_max_average_rent_per_unit, gl_max_average_rent_per_unit])

    for a,b,i in zip(x, y, range(len(x))):
        plt.text(a, b, "%.2f"%y[i], ha = 'center', va = 'bottom')
    plt.bar(x, y, width = 0.5)
    plt.title('各地最高单位面积租金(元/平米)')
    plt.subplot(2, 2, 2)

def min_rent_per_unit(bj_rent_per_unit, sh_rent_per_unit, gz_rent_per_unit, sz_rent_per_unit, gl_rent_per_unit):
    bj_min_average_rent_per_unit = min(bj_rent_per_unit)
    sh_min_average_rent_per_unit = min(sh_rent_per_unit)
    gz_min_average_rent_per_unit = min(gz_rent_per_unit)
    sz_min_average_rent_per_unit = min(sz_rent_per_unit)
    gl_min_average_rent_per_unit = min(gl_rent_per_unit)
    x = np.array(["北京最低单位面积租金", "上海最低单位面积租金", "广州最低单位面积租金", "深圳最低单位面积租金", "桂林最低单位面积租金"])
    y = np.array([bj_min_average_rent_per_unit, sh_min_average_rent_per_unit, gz_min_average_rent_per_unit, sz_min_average_rent_per_unit, gl_min_average_rent_per_unit])

    for a,b,i in zip(x, y, range(len(x))):
        plt.text(a, b, "%.2f"%y[i], ha = 'center', va = 'bottom')
    plt.bar(x, y, width = 0.5)
    plt.title('各地最低单位面积租金(元/平米)')
    plt.subplot(2, 2, 3)

def median_rent_per_unit(bj_rent_per_unit, sh_rent_per_unit, gz_rent_per_unit, sz_rent_per_unit, gl_rent_per_unit):
    bj_median_average_rent_per_unit = np.median(bj_rent_per_unit)
    sh_median_average_rent_per_unit = np.median(sh_rent_per_unit)
    gz_median_average_rent_per_unit = np.median(gz_rent_per_unit)
    sz_median_average_rent_per_unit = np.median(sz_rent_per_unit)
    gl_median_average_rent_per_unit = np.median(gl_rent_per_unit)
    x = np.array(["北京单位面积租金中位数", "上海单位面积租金中位数", "广州单位面积租金中位数", "深圳单位面积租金中位数", "桂林单位面积租金中位数"])
    y = np.array([bj_median_average_rent_per_unit, sh_median_average_rent_per_unit, gz_median_average_rent_per_unit, sz_median_average_rent_per_unit, gl_median_average_rent_per_unit])

    for a,b,i in zip(x, y, range(len(x))):
        plt.text(a, b, "%.2f"%y[i], ha = 'center', va = 'bottom')
    plt.bar(x, y, width = 0.5)
    plt.title('各地单位面积租金中位数(元/平米)')
    plt.subplot(2, 2, 4)

df_bj = pd.read_csv('./final_data/bj.csv')
df_sh = pd.read_csv('./final_data/sh.csv')
df_gz = pd.read_csv('./final_data/gz.csv')
df_sz = pd.read_csv('./final_data/sz.csv')
df_gl = pd.read_csv('./final_data/gl.csv')

average_rent(df_bj, df_sh, df_gz, df_sz, df_gl)
max_rent(df_bj, df_sh, df_gz, df_sz, df_gl)
min_rent(df_bj, df_sh, df_gz, df_sz, df_gl)
median_rent(df_bj, df_sh, df_gz, df_sz, df_gl)
average_rent(df_bj, df_sh, df_gz, df_sz, df_gl)
plt.show()

bj_rent_per_unit = list(df_bj['月租'] / df_bj['面积'])
sh_rent_per_unit = list(df_sh['月租'] / df_sh['面积'])
gz_rent_per_unit = list(df_gz['月租'] / df_gz['面积'])
sz_rent_per_unit = list(df_sz['月租'] / df_sz['面积'])
gl_rent_per_unit = list(df_gl['月租'] / df_gl['面积'])

average_rent_per_unit(bj_rent_per_unit, sh_rent_per_unit, gz_rent_per_unit, sz_rent_per_unit, gl_rent_per_unit)
max_rent_per_unit(bj_rent_per_unit, sh_rent_per_unit, gz_rent_per_unit, sz_rent_per_unit, gl_rent_per_unit)
min_rent_per_unit(bj_rent_per_unit, sh_rent_per_unit, gz_rent_per_unit, sz_rent_per_unit, gl_rent_per_unit)
median_rent_per_unit(bj_rent_per_unit, sh_rent_per_unit, gz_rent_per_unit, sz_rent_per_unit, gl_rent_per_unit)
average_rent_per_unit(bj_rent_per_unit, sh_rent_per_unit, gz_rent_per_unit, sz_rent_per_unit, gl_rent_per_unit)
plt.show()
