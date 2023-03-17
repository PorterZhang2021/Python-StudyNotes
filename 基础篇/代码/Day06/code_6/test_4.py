from module2 import foo
from module1 import foo

# 因为module1是后引入的
# 输出hello,world!
foo()