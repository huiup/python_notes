from enum import Enum
# 枚举的转换
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    RED = 4
a = 1
print(VIP(a))
print(VIP(a).name)