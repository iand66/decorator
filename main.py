def f1(func):
    def wrapper(*args, **kwargs):
        print("Started ...")
        func(*args, **kwargs)
        print("Ended ...")
    return wrapper

def f():
    print("Hello")

@f1
def x(msg):
    print(msg)

# Direct Call
f1(f)
f1(f)()

# Aliasing
f = f1(f)
f()

x("At last I get it")