import pytest

#创建一个登陆的fixture方法，yield关键字激活了fixture的teardown方法
@pytest.fixture(scope="module",autouse=True)
def login():
    print("登陆操作")
    print("获取token")
    username = 'tom'
    password = '12345678'
#    return [username, password]
    yield [username, password]
    print("登出操作")

#测试用例1： 需要提前登陆
def test_case1(login,connectDB):
    print(f"user name and name: {login}")
    print("测试用例：1")

#测试用例2： 不需要提前登陆
def test_case2():
    print("测试用例：2")

#测试用例3： 需要提前登陆
def test_case3(login):
    print("测试用例：3")

