"""
作业1：
1、编写用例顺序：加- 除-减-乘
2、控制测试用例顺序按照【加-减-乘-除】这个顺序执行
"""

import pytest

@pytest.mark.parametrize("a",[1],ids=['整数'])
@pytest.mark.run(order = 1)
def test_add(a):
    print(a)
    print("add case")

@pytest.mark.run(order = 4)
def test_div():
    print("div case")

@pytest.mark.run(order = 2)
def test_sub():
    print("sub case")

@pytest.mark.run(order = 3)
def test_mul():
    print("mult case")
