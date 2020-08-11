import pytest


"""
1、注册一个命令行参数env，定义分组hogwarts ,将参数 env放在hogwards分组下
"""
def pytest_addoption(parser: "Parser", pluginmanager: "PytestPluginManager") -> None:
    mygroup = parser.getgroup("hogwarts")  #group将下面所有的option都展示在这个group下
    mygroup.addoption("--env",
                      default = 'test',
                      dest = 'dev' or 'st',
                      help = 'set your run env'
                      )

@pytest.fixture(scope="session")
def cmdoption(request):
    return request.config.getoption("--env",default='test')