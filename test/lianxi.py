# -*- coding: utf-8 -*-
_author_='fh'

s=[1,2,3,4,5,6,7,8,9,10]
def os(t):
    return t % 2==0

if __name__ == "__main__":
    news=filter(os,s)
print(list(news))
