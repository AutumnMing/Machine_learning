
import pandas as pd 
import numpy as np

# 自定义统计方法


def missing(df):
    '''
    - df : 传入数据框
    - 默认返回存在缺失值的列；
    - 对缺失值进行了排序  
    '''
    miss = pd.DataFrame(df.isnull().sum(), columns = ['missing']) # 缺失值计算
    miss = miss.reset_index(drop=False) # 将索引取出, 通过设置drop=False保留原索引名称, 即列名
    miss = miss.sort_values(by='missing', ascending=False) # 按照缺失值进行排序
    miss.rename(columns={'index':'var_name'}, inplace=True)
    miss['per'] = np.around(miss['missing']*100 / len(df),2) # 缺失值占比
    miss = miss.query('missing > 0').reset_index(drop=True) 
    print(f'''缺失值var_name: {miss['var_name'].tolist()}''')
    
    return miss 