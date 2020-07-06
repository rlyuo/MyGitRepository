# coding=utf-8

def function_1(A):
    print("function_1")


def function_2(B):
    print(B(3))
    print("function_2")


@function_1
@function_2
def function_name(n):
    print("Hello World ,i am function_name")
    return n + 5



# python会按照自上而下的顺序把各自的函数结果作为下一个函数的输入。
# 输出结果：

"""
hello world ,i am function_name
8
function_2
function_1
"""


def log(func):
    def wrapper():
        print('log开始 ...')
        func()
        print('log结束 ...')

    return wrapper


@log
def test1():
    print('test1 ..')


def test2():
    print('test2 ..')


print(test1.__name__)
print(test2.__name__)



def funA(a):
    print('funA')

def funB(b):
    print('funB')

@funA
@funB
def funC():
    print('funC')

funA(funB(funC))



def myFunction():
    print('变量 __name__ 的值是 ' + __name__)
def main():
    myFunction()
if __name__ == '__main__':
    main()