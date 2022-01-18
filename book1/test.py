# wine数据集变量
variable = [
    'Alcohol', 'Malic_acid', 'Ash', 'Alcalinity_of_ash', 'Magnesium', 'Total_phenols',
    'Flavanoids', 'Nonflavanoid_phenols', 'Proanthocyanins', 'Color_intensity', 'Hue', 'diluted wines', 
    'Proline'
]

names = [
    '酒精', '苹果酸', '灰', '灰的碱度', '镁', '总酚类化合物', '类黄酮', 
    'Nonflavanoid酚类', '原花青素', '颜色强度', '色调', 
    '稀释葡萄酒的OD280/OD315', '脯氨酸'
]

import pandas as pd 
df = pd.DataFrame()

df = df.iloc[:,:]

print(pd.__name__)

df = pd.read_csv(header=None)