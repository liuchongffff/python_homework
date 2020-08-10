import pytest

#5、将 Fixture 方法存放在conftest.py ，灵活设置scope的级别

#4, 创建 Fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
import yaml
from test_pytest_first_day.calc import Calculator

@pytest.fixture(scope ="function")
def add_comment():
    print("开始计算")
    yield
    print("结束计算")


#2、使用fixture方法，完成加减乘除用例的自动生成，添加别名
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