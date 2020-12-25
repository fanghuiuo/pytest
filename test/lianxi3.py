# -*- coding: utf-8 -*-
_author_='fh'
lt=[1,2,3,4,5,6,7,8,9,10]
def os(n):
    return n % 2 ==0
def pf(n):
    return n*n
if __name__ == "__main__":
    newlt=map(pf,list(filter(os,lt)))
    print(list(newlt))