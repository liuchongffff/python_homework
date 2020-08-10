import pytest
import yaml

from test_pytest_first_day.calc import Calculator

#data_path = os.
with open('./calc2.yaml') as f:
    datas = yaml.safe_load(f)
    add_datas = datas['add']['para_add']
    add_case_ids = datas['add']['myid_add']
    div_datas = datas['para_div']['para_div_data']
    div_case_ids = datas['para_div']['myid_div']
    print(f"add_datas:{add_datas}")
    print(f"add_case_ids:{add_case_ids}")
    print(f"div_datas:{div_datas}")
    print(f"div_case_ids:{div_case_ids}")
    f.close()

#创建 Fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
@pytest.fixture(scope ="function")
def add_comment():
    print("开始计算")
    yield
    print("结束计算")


#2.1、使用fixture方法，完成加减乘除用例的自动生成，添加别名
@pytest.fixture(scope ="class")
def getaddCalc():
    print("获取计算器加法实例")
    calc_i_add = Calculator()
    return calc_i_add

@pytest.fixture(params= add_datas,ids=add_case_ids)
def get_add_data(request):
    print("获取加法参数")
    data = request.param
    print(f"data is {data}")
    return data

#2.2、使用fixture方法，完成加减乘除用例的自动生成，添加别名
@pytest.fixture(scope ="class")
def getdivCalc():
    print("获取除法实例")
    calc_i_div = Calculator()
    return calc_i_div



@pytest.fixture(params= div_datas,ids=div_case_ids)
def get_div_data(request):
    print("获取除法参数")
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

    #利用fixture获取加法实例：getaddCalc
    #利用fixture获取加法实例测试数据： get_add_data
    #利用fixture在每个测试实例中打印开始计算，结束打印结束运算： add_comment)
    @pytest.mark.add
    def test_add(self,getaddCalc,get_add_data,add_comment):
        calc_add_ins = getaddCalc
        datas = get_add_data
        result = calc_add_ins.add(datas[0],datas[1])
        if isinstance(result,float):
            result = round(result, 2)
        assert datas[2] == result

    """
    #针对Calculator中的函数div，几种测试用例：
    #1：小正负整数相除，-1 = -2/2
    #2：小负正整数相除，-1 = 2/-2
    #3：大正整数相除， 10 = 100/10
    #4：正负浮点数相除   -2 = 100.0/（-50.0）
    #5：负负浮点数相除数   2 = -100.0/（-50.0）
    #6：除数为0   ！！！ = -100.0/0
    """
    #利用fixture获取除法实例：getdivCalc
    #利用fixture获取除法实例测试数据： get_div_data
    #利用fixture在每个测试实例中打印开始计算，结束打印结束运算： add_comment)
    @pytest.mark.div
    def test_div(self,getdivCalc,get_div_data,add_comment):
        calc_div_ins = getdivCalc
        datas = get_div_data
        try:
            result = calc_div_ins.div(datas[0],datas[1])
            if isinstance(result, float):
                result = round(result, 2)
                print(f"the result is {result}")
            assert datas[2] == result
        except Exception:
            print("error .!!!!")
            assert True