#!/usr/bin/env python
# encoding: utf-8
"""
作者: 王海虹
日期: 2021/1/19 9:28 下午
简介: 测试用例 执行结构(setup和teardown)

    模块级（setup_module/teardown_module）开始于模块始末，全局的

    函数级（setup_function/teardown_function）只对函数用例生效（不在类中）

    类级（setup_class/teardown_class）只在类中前后运行一次(在类中)

    方法级（setup_method/teardown_method）开始于方法始末（在类中）

    类里面的（setup/teardown）运行在调用方法的前后
"""

import pytest


# 类和方法
class TestCase():
    def setup(self):
        print("setup: 每个用例开始前执行")

    def teardown(self):
        print("teardown: 每个用例结束后执行")

    def setup_class(self):
        print("setup_class: 所有用例执行之前")

    def teardown_class(self):
        print("teardown_class: 所有用例结束后执行")

    def setup_method(self):
        print("setup_method:  每个用例开始前执行")

    def teardown_method(self):
        print("teardown_method:  每个用例结束后执行")

    def test_one(self):
        print("正在执行----test_one")
        x = "this"
        assert 'h' in x

    def test_two(self):
        print("正在执行----test_two")
        x = "hello"
        assert 'o' in x

    def test_three(self):
        print("正在执行----test_three")
        a = "hello"
        b = "hello world"
        assert a in b


if __name__ == "__main__":
    # -s: 显示用例的打印信息，-q：只显示结果
    pytest.main(["-s", "test_fixtclass.py"])
