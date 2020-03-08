# 可变关键字参数
def func_kwargs(args1, **kwargs):
    print("args1:", args1)
    for key in kwargs:
        print("keyword arg: %s : %s" % (key, kwargs[key]))
func_kwargs(9527 ,birth=1997, name='zhang',请回答1988 = '闭嘴吧1997')