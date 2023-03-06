# 列表生成式语法
import sys

f = [x for x in range(1, 10)]
print(f)

# 利用两个生成，合并出想要的结果 函数式编程
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)

# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素就已经准备就绪
# 所以需要耗费较多的内存空间
f = [x ** 2 for x in range(1, 1000)]
# 查看对象占用的内存字节数
print(sys.getsizeof(f))
print(f)

# 请注意下面的代码创建的不是一个列表而是一个生成器对象
# 通过生成器可以获取到数据但它不占用额外的空间存储器
# 每次需要数据的时候就通过内部的运算得到数据（需要花费额外的时间）
f = (x ** 2 for x in range(1, 1000))
# 相比生成式生成器不占用存储数据的空间
print(sys.getsizeof(f))
print(f)

for val in f:
    print(val)
