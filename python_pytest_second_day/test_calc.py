import pytest

from test_pytest_first_day.calc import Calculator
from python_pytest_second_day.caculator2 import Calculator_two


@pytest.fixture(scope ="class")
def getCalc():
    print("获取计算器实例")
    calc_i = Calculator()
    return calc_i

@pytest.fixture(params=[
        (-100,-100,-200),
        (-1, -1, -2),
        (1, 1, 2),
        (100, 100, 200),
        (1.5, 1.32, 2.82),
        (-1.5, -1.32, -2.82)
    ],ids=["test_add1","test_add2","test_add3","test_add4","test_add5","test_add6"])
def get_data(request):
    print("获取参数")
    data = request.param
    print(f"data is {data}")
    return data

class TestCalc:
    """
    #针对Calculator中的函数add，几种测试用例：
    #1：小负整数相加 -200 = -100+（-100）
    #2：大负整数相加 -2 = -1+（-1）
    #3：小正整数相加， 2 = 1+1
    #4：大正整数， 200 = 100 + 100
    #5：正浮点数想加: 2.82 = 1.5 + 1.32
    #6：负浮点数相加: -2.82 = -1.5 + -1.32
    """
    @pytest.mark.add
    def test_add(self,getCalc,get_data):
        calc_ins = getCalc
        datas = get_data
        result = calc_ins.add(datas[0],datas[1])
        if isinstance(result,float):
            result = round(result, 2)
        assert datas[2] == result
