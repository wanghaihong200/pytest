#!/usr/bin/env python
# encoding: utf-8
"""
作者: 王海虹
日期: 2021/1/22 9:35 下午
简介:
"""
import pytest


class TestCase():
    def test_s1(self, login):
        print("用例1：登录之后其它动作111")

    def test_s2(self):  # 不传login
        print("用例2：不需要登录，操作222")

    def test_s3(self, login):
        print("用例3：登录之后其它动作333")


if __name__ == "__main__":
    pytest.main(["-s", "test_fix1.py"])
