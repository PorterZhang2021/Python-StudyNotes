# 导入包
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

    # 访问器
    @property
    def face(self):
        return self._face

    # 访问器
    @property
    def suite(self):
        return self._suite

    # 面值显示
    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        # 返回值
        return face_str

    # 返回值
    def __repr__(self):
        return self.__str__()


# 一副牌
class Poker(object):
    """一副牌"""

    # 初始化
    def __init__(self):
        self._cards = [Card(suite, face)
                       for suite in '♠♥♣♦'
                       for face in range(1, 14)]
        self._current = 0

    # 访问器
    @property
    def cards(self):
        return self._cards

    # 洗牌器
    def shuffle(self):
        """洗牌(随机乱序)"""
        self._current = 0
        random.shuffle(self._cards)

    # 访问器
    @property
    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card

    # 访问器
    @property
    def has_next(self):
        """还没有牌"""
        return self._current < len(self._cards)


# 玩家
class Player(object):
    """玩家"""

    # 初始化
    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    # 访问器
    @property
    def name(self):
        return self._name

    # 访问器
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
def main():
    p = Poker()
    # 洗牌
    p.shuffle()
    # 玩家
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]

    # 轮次发牌
    for _ in range(13):
        # 每个玩家轮次发牌
        for player in players:
            # 这里利用了生成器的next功能
            player.get(p.next)

    # 输出每个玩家手里的牌
    for player in players:
        print(player.name + ':', end=' ')
        # 整理玩家手中的牌
        player.arrange(get_key)
        # 返回玩家手里持有的牌
        print(player.cards_on_hand)


# 开始
if __name__ == '__main__':
    main()
