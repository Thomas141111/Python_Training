def decor1(fun):
    def inner(*args,**kwargs):
        print("IN DECOR1")
        fun(*args,**kwargs)
        print("IN decor1.2")
    return inner

def decor2(fun):
    def inner(*args,**kwargs):
        print("In DEcor2")
        fun(*args,**kwargs)
        print("In decor2.1")
    return inner

@decor1
@decor2
def fun(msg):
    print("In fun")

fun("jn")