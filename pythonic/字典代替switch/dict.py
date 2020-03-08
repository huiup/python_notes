""" 
day = 6
switcher = {
    0 : 'Sunday',
    1 : 'Monday',
    2 : 'Tuesday'
}
用get方法解决key值不存在的情况（即switch中的default）
day_name = switcher.get(day,'unknown')
print(day_name)
但此方法不能解决switch中出现代码块的情况，解决如下： 
"""
day = 0
def get_sunday():
    return 'Sunday'
def get_monday():
    return 'Monday'
def get_tuesday():
    return 'Tuesday'
def get_default():
    return 'Unknown'
switcher = {
    0 : get_sunday,
    1 : get_monday,
    2 : get_tuesday
}
day_name = switcher.get(day,get_default)()
print(day_name)