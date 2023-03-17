from time import sleep
from threading import Thread, Lock

class Account(object):

    # 初始化
    def __init__(self):
        self._balance = 0
        self._lock = Lock()
    
    def deposit(self, money):
        # 先获取锁才能执行后续的代码
        self._lock.acquire()
        # 异常捕获
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()
    
    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        # 初始化
        super().__init__()
        self._account = account
        self._money = money
    
    def run(self):
        self._account.deposit(self._money)

def main():
    # 主函数
    # 创建账户
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        # 开始
        t.start()
    for t in threads:
        t.join()
    print('账户余额: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()