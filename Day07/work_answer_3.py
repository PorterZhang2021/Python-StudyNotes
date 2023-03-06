"""
设计一个函数返回给定文件名的后缀名
"""


def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """

    # 按右方寻找到.的位置截止
    pos = filename.rfind('.')
    # 如果pos大于0或者小于等于文件长度
    if 0 < pos < len(filename) - 1:
        # 判断has_dot是否需要保存.
        index = pos if has_dot else pos + 1
        # 返回文件后缀
        return filename[index:]
    else:
        # 返回空
        return ''
