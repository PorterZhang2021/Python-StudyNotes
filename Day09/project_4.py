"""
21点游戏
"""
import random

# 牌类
class Card(object):
    """一张牌"""

    # 初始化
    def __init__(self, suite, face):
        # 花色
        self._suite = suite
        # 面值
        self._face = face
    
    # 获取面值
    @property
    def face(self):
        return self._face

    # 获取花色
    @property
    def suite(self):
        return self._suite
    
    # 显示面值
    def __str__(self):
        # A
        if self._face == 1:
            face_str = 'A'
        # J
        elif self._face == 11:
            face_str = 'J'
        # Q
        elif self._face == 12:
            face_str = 'Q'
        # K
        elif self._face == 13:
            face_str = 'K'
        # 其他
        else:
            face_str = str(self._face)
        
        # 返回值
        return face_str
    
    # 返回值
    def __repr__(self):
        return self.__str__()
    

# 一副牌
class Poker(object):
    
    # 初始化
    def __init__(self):
        # 一整副牌
        self._cards = [Card(suite, face)
                       for suite in '♠♥♣♦'
                       for face in range(1, 14)]
        self._current = 0
    
    # 访问牌
    @property
    def cards(self):
        return self._cards
    
    # 洗牌器
    def shuffle(self):
        """洗牌(随机乱序)"""
        self._current = 0
        random.shuffle(self._cards)
    
    # 发牌
    @property
    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card

    # 是否有牌
    @property
    def has_next(self):
        """是否有牌"""
        return self._current < len(self._cards)
    

# 玩家
class Player(object):
    """玩家"""

    # 初始化
    def __init__(self, name):
        # 名字
        self._name = name
        # 手牌
        self._cards_on_hand = []
    
    # 获取名字
    @property
    def name(self):
        return self._name

    # 获取手牌
    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    # 摸牌
    def get(self, card):
        """摸牌"""
        self._cards_on_hand.append(card)
    
    # 整理牌
    def arrange(self, card_key):
        """玩家整理手上的牌"""
        self._cards_on_hand.sort(key=card_key)

# 排序规则 - 先根据花色再根据点数排序
def get_key(card):
    return (card.suite, card.face)

# 主函数
## 21点游戏开发

