import pandas as pd
# 利用pands读取文件
df = pd.read_csv('data.csv')
# 输出文件
print(df)
# 转化为列表输出
data = df.values.tolist()
print(data)

# 逐行遍历获取结果
for index, row in df.iterrows():
    print(row.tolist())
    