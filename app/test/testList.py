#! usr/bin/env python
#-*- coding :utf-8 -*-
L = ['a','b','c','d']

print(L)
print("L[0] = "  + L[0])
print("L[-1] = " + L[-1])
print(L[0:2])
print(L[:-1])
print(L[-2:])


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x for x in L1 if isinstance(x,str)]
print(L2)