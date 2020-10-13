from enum import Enum
# 枚举之间的比较
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    RED = 4
class VIP1(Enum):
    YELLOW = 1
    GREEN = 1
    RED = 4
# for v in VIP1.__members__:
#     print(v)
# result = VIP.GREEN > VIP.GREEN 会报错
result = VIP.GREEN == VIP.GREEN
print(result)
result = VIP.GREEN == VIP1.GREEN
print(result)
result = VIP.GREEN is VIP.GREEN
print(result)
