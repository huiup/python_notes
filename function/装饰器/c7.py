# 可变位置参数*args
def func_arg(args1, *args):
    print("args1:", args1)
    for arg in args:
        print("another arg:", arg)
func_arg('zhang','666',"淦",'火之高兴','霜之哀伤',666)