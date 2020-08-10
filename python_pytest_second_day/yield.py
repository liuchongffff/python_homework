

#yield生成器,next来获取生成器里面的下一个值
def provider():
    for i in range(0,10):
        print("开始操作")
        yield i
        print("结束操作")

p = provider()
print(p)
print(next(p))
print(next(p))
print(next(p))
print(next(p))



