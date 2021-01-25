#!/usr/bin/env python
# encoding: utf-8
"""
作者: 王海虹
日期: 2021/1/22 9:30 下午
简介: 如果有多个.py的文件都需要调用这个登陆功能的话，那就不能把登陆写到用例里面去了。
    此时应该要有一个配置文件，单独管理一些预置的操作场景，pytest里面默认读取conftest.py里面的配置

    conftest.py配置需要注意以下点：

        conftest.py配置脚本名称是固定的，不能改名称
        conftest.py与运行的用例要在同一个pakage下，并且有__init__.py文件
        不需要import导入 conftest.py，pytest用例会自动查找
"""

import pytest

@pytest.fixture()
def login():
    print("输入账号，密码先登录")
