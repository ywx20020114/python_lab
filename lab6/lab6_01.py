
def func_out(time):
    def decorator(func):
        def wapper(*args,**kwargs):
            count=0
            while count<time:
                func(*args,**kwargs)
                count+=1
        return wapper
    return decorator

time = int(input("请输入重复的次数"))
@ func_out(time)
def foo():
    print("this is foo")
foo()
