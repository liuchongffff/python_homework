from test_pytest_first_day.calc import Calculator

"""
#针对Calculator中的函数add，几种测试用例：
1：小负整数相加，
2：大负整数相加，
3：小正整数相加，
4：大正整数
5：正浮点数想加
6：负浮点数相加
"""

#1：小负整数相加 -200 = -100+（-100）
def test_add1 ():
    i_calc = Calculator()
    result = i_calc.add(-100,-100)
    assert -200 == result

#2：大负整数相加 -2 = -1+（-1）
def test_add2 ():
    i_calc = Calculator()
    result = i_calc.add(-1,-1)
    assert -2 == result

#3：小正整数相加， 2 = 1+1
def test_add3 ():
    i_calc = Calculator()
    result = i_calc.add(1,1)
    assert 2 == result

#4：大正整数， 200 = 100 + 100
def test_add4 ():
    i_calc = Calculator()
    result = i_calc.add(100,100)
    assert 200 == result

#5：正浮点数想加: 2.82 = 1.5 + 1.32
def test_add5 ():
    i_calc = Calculator()
    result = i_calc.add(1.5,1.32)
    if isinstance(result,float):
        result = round(result, 2)
    assert 2.82 == result

#6：负浮点数相加: -2.82 = -1.5 + -1.32
def test_add6 ():
    i_calc = Calculator()
    result = i_calc.add(-1.5,-1.32)
    if isinstance(result,float):
        result = round(result, 2)
        print(f"result : {result}")
    assert -2.82 == result



"""
#针对Calculator中的函数div，几种测试用例：
1：小正负整数相除，-1 = -2/2
2：小负正整数相除，-1 = 2/-2
3：大正整数相除， 1 = 100/10
4：正负浮点数相除   -2 = 100.0/（-50.0）
5：负负浮点数相除数   2 = -100.0/（-50.0）
"""
#1：小正负整数相除，-1 = -2/2
def test_div1 ():
    i_calc = Calculator()
    result = i_calc.div(-2,2)
    assert -1 == result

#2：小负正整数相除，-1 = 2/-2
def test_div2 ():
    i_calc = Calculator()
    result = i_calc.div(2,-2)
    assert -1 == result

#3：大正整数相除， 10 = 100/10
def test_div3 ():
    i_calc = Calculator()
    result = i_calc.div(100,10)
    assert 10 == result

#4：正负浮点数相除   -2 = 100.0/（-50.0）
def test_div4 ():
    i_calc = Calculator()
    result = i_calc.div(100.0,-50.0)
    assert -2.0 == result

#5：负负浮点数相除数   2 = -100.0/（-50.0）
def test_div5 ():
    i_calc = Calculator()
    result = i_calc.div(-100.0,-50.0)
    assert 2.0 == result

#6：除数为0   ！！！ = -100.0/0
def test_div6 ():
    i_calc = Calculator()
    try:
        result = i_calc.div(-100,0)
    except Exception:
        print("error ,")
        assert True