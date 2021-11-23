# -*- coding: utf-8 -*-
def bisec(f,a,b,N):
    an=a
    bn=b
    fan=f(an)
    fbn=f(bn)
    for i in range(N):
        cn=(an+bn)/2.0
        fcn=f(cn) 
        if fcn==0:
            return cn
        elif fan*fcn<0:
            bn=cn
            fbn=fcn
        else:
            an=cn
            fan=fcn
    return cn