#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @CharactersTime  : 2019/12/9 10:17
# @Author: Jtyoui@qq.com
from pyunit_time import CharactersTime


def time():
    """字符字符串时间解析"""
    print(CharactersTime('2019-12-19 00:00:00').parse('国庆节的前一天晚上8点半'))  # ['2019-09-29 20:30:00']
    print(CharactersTime('2019-12-19 00:00:00').parse('今天晚上8点'))  # ['2019-12-19 20:00:00']
    print(CharactersTime('2019-12-19 00:00:00').parse('今年儿童节晚上九点一刻'))  # ['2019-06-01 21:15:00']
    print(CharactersTime('2019-12-19 00:00:00').parse('今天中午十二点'))  # ['2019-12-19 12:00:00']
    print(CharactersTime('2019-12-19 00:00:00').parse('明年春节'))  # ['2020-01-25 00:00:00']
    print(CharactersTime('2019-12-19 00:00:00').parse('下下下个星期五早上7点半'))  # ['2020-01-10 07:30:00']
    print(CharactersTime('2019-12-19 00:00:00').parse('今年的大寒'))  # ['2020-01-20 00:00:00']
    print(CharactersTime('2019-12-19 00:00:00').parse('2019年12月'))  # ['2019-12-01 00:00:00']
    print(CharactersTime('2019-12-19 00:00:00').parse('19-2-2'))  # ['2019-02-02 00:00:00']
    print(CharactersTime('2019-12-19 00:00:00').parse('2020-2'))  # ['2020-02-01 00:00:00']
    print(CharactersTime('2019-12-19 00:00:00').parse('8年前'))  # ['2011-12-19 00:00:00']
    print(CharactersTime('2019-12-19 00:00:00').parse('最近'))  # []
    print(CharactersTime('2019-12-19 00:00:00').parse('三天以后'))  # ['2019-12-22 00:00:00']
    print(CharactersTime('2019-12-19 00:00:00').parse('三天之内的下午3点'))  # ['2019-12-22 15:00:00']


if __name__ == '__main__':
    time()
