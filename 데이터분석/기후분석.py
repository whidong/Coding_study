import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


df = pd.read_csv('C:/python open space/데이터분석\대기과학csv파일/ta_20221118165508xls.csv', encoding='euc-kr')
df
bar1 = df.plot.barh(x='년월', y='평균기온(℃)',rot=0, figsize=(10,5),title='기상분석')
print(bar1)
bar1.show

