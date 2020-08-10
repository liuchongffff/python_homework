import pytest

#5、将 Fixture 方法存放在conftest.py ，灵活设置scope的级别
@pytest.fixture(scope = "session")
def connectDB():
    print("连接数据库操作")
    yield
    print("断开数据库操作")