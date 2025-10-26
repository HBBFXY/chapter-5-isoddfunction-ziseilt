def isOdd(x):
    # 首先检查是否为整数类型
    if not isinstance(x, int):
        return False
    
    # 然后检查是否为奇数
    return x % 2 != 0
