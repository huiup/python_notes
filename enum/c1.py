from enum import Enum
# 枚举 在python中，枚举是一个类
# 防止可变的功能
# 防止相同标签的功能
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    RED = 4
class VIP2(Enum):
    YELLOW = 1
    GREEN = 1
    RED = 4
# print(VIP.YELLOW)
# print(type(VIP.YELLOW))
# #获取枚举的名称
print(VIP.YELLOW.name)
# print(type(VIP.YELLOW.name))
# #获取枚举的值
# print(VIP.YELLOW.value)
# print(type(VIP.YELLOW.value))
# # 获取名称所对应的枚举类型
# print(VIP['GREEN'])
# print(type(VIP['GREEN']))

