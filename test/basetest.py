# -*- coding: utf-8 -*-
'测试用'
_author_='fh'

age=input("please input your age:")


def szdx(x):
    
    t=int(x)
    if t>20 and t<30:
        print("大于20小于30")
    elif t<=20 or t >=30:
        print("小于等于20或者大于等于30")
    
    
if __name__ == "__main__":
    szdx(age)