# encoding: utf-8
"""
@author: lileilei
@site: 
@software: PyCharm
@file: data_yaml.py
@time: 2017/8/14 13:16
"""
def data(f):
    m=open(f,'rb')
    return (eval(m.readline().decode('utf-8'))['data'])
