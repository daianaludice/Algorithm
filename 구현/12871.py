#https://www.acmicpc.net/problem/12871
a = input()
b = input()

s = len(a)
t = len(b)

A = a*t
B = b*s

if A == B:
    print(1)
else:
    print(0)
