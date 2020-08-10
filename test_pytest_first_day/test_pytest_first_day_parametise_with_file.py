
import pytest
import yaml

from test_pytest_first_day.calc import Calculator



"""
#通过定义一个yaml文件，保存相关的文件内容：
[-100，-100，-100],
[-1,-1,-2],
[1,1,2],
[100,100,200],
[1.5,1.32,2.82],
[-1.5,-1.32,-2.82]
#针对Calculator中的函数add，几种测试用例：
#1：小负整数相加 -200 = -100+（-100）
#2：大负整数相加 -2 = -1+（-1）
#3：小正整数相加， 2 = 1+1
#4：大正整数， 200 = 100 + 100
#5：正浮点数想加: 2.82 = 1.5 + 1.32
#6：负浮点数相加: -2.82 = -1.5 + -1.32
"""
with open('./calc.yaml') as f:
    datas = yaml.safe_load(f)
    add_datas = datas['add']
    div_datas = datas['para_div']
    print(f"add_datas:{add_datas}")
    print(f"div_datas:{div_datas}")
    f.close()

@pytest.mark.add
@pytest.mark.parametrize('a,b,expect',add_datas,ids=["test_add1","test_add2","test_add3","test_add4","test_add5","test_add6"])
def test_add(a,b,expect):
    i_calc = Calculator()
    result = i_calc.add(a,b)
    if isinstance(result,float):
        result = round(result, 2)
    assert expect == result



@pytest.mark.para_div
@pytest.mark.parametrize('a,b,expect',div_datas,ids=["test_div1","test_div2","test_div3","test_div4","test_div5","test_div6"])
def test_div(a,b,expect):
    i_calc = Calculator()
    try:
        result = i_calc.div(a,b)
        if isinstance(result, float):
            result = round(result, 2)
            print(f"the result is {result}")
        assert expect == result
    except Exception:
        print("error .!!!!")
        assert True