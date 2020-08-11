
"""
作业2【选做】：
1、注册一个命令行参数env，定义分组hogwarts ,将参数 env放在hogwards分组下
2、env默认值是test,表示测试环境，另外还有两个值 （dev,st）不同的环境读取不同的数据
"""

def test_addoption(cmdoption):

    print(f"this --env : {cmdoption}")