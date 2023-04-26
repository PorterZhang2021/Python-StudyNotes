import pandas as pd

# 数据文件
data = [
    {'id': '1001', 'name': 'Mike', 'age': 20},
    {'id': '1002', 'name': 'Bob', 'age': 22},
    {'id': '1003', 'name': 'Jordan', 'age': 21},
]
# 构建一个DataFrame对象
df = pd.DataFrame(data)
# 调用to_csv方法存储数据
df.to_csv('data.csv', index=False)