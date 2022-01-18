# 一些处理函数
import pandas as pd
import seaborn as sns
import numpy as np
import os


def my_pd_setting():
    '''
    - pandas相关设置
    '''
    pd.set_option( 'display.precision',2)
    pd.set_option("display.max_rows",999)  # 最多显示行数
    pd.set_option("display.min_rows",20)   # 最少显示行数
    pd.set_option('display.max_columns',None)  # 全部列
    pd.set_option ('display.max_colwidth', None)   # 修改列宽
    pd.set_option("expand_frame_repr", True)  # 折叠
    # pd.options.plotting.backend = "plotly"  # 修改绘图
    pd.set_option("colheader_justify","left")  # 列字段对齐方式
    # 不写返回值，即返回None
    print(f'''{pd.__name__}的版本为: {pd.__version__}''')

    return

def my_sns_setting():
    '''
    -rc 解决不显示中文字体的问题

    '''
    sns.set_theme()
    rc = {
        'font.sans-serif': 'SimHei',
        'axes.unicode_minus': False
    }
    sns.set( rc=rc) 
    print(f'''{sns.__name__}的版本为: {sns.__version__}''')
    return


def my_np_setting():

    print(f'''{np.__name__}的版本为{np.__version__}''')
    return 


def data_path(filepath):
    '''
    - filepath: 路径
    - filename: 文件名
    '''
    os.chdir(filepath)
    filename=os.listdir(filepath)
    print(f'''当前数据路径为: {os.getcwd()}''')
    return filename