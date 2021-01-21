#!/usr/bin/env python
# encoding: utf-8
"""
作者: 王海虹
日期: 2021/1/21 8:24 下午
简介: 自定义测试用例的预置条件
    firture相对于setup和teardown来说应该有以下几点优势:

        命名方式灵活，不局限于setup和teardown这几个命名
        conftest.py 配置里可以实现数据共享，不需要import就能自动找到一些配置
        scope="module" 可以实现多个.py跨文件共享前置, 每一个.py文件调用一次
        scope="session" 以实现多个.py跨文件使用一个session来完成多个用例
"""
import pytest


class TestCase():
    @pytest.fixture(scope="function")
    def login(self):
        print("输入账号，密码登录")

    @pytest.fixture(scope="class")
    def login2(self):
        print("输入账号1，密码登录")

    def test_s1(self, login):
        print("用例1：登录之后其它动作111")

    def test_s2(self):  # 不传login
        print("用例2：不需要登录，操作222")

    def test_s3(self, login):
        print("用例3：登录之后其它动作333")



if __name__ == "__main__":
    pytest.main(["-s", "test_fix.py"])
