import pytest



def test_c(connectDB):
    print("测试用例c")

class TestDemo:
    def test_a(self,connectDB):
        print("测试用例a")

    def test_b(self,connectDB):
        print("测试用例b")

class TestDemo1:
    def test_a(self,connectDB):
        print("测试用例a")

    def test_b(self,connectDB):
        print("测试用例b")

