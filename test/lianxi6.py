# -*- coding: utf-8 -*-
_author_='fh'

def cfb(n):
    lt=['']
    for i in range(1,n+1):
        for j in range(1,n+1):
            lt.append('%s * %s=%s' % (i,j,i*j))
    
    print(lt)
if __name__ == "__main__":
    cfb(10)