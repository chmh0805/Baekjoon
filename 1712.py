import sys
A,B,C = map(int, sys.stdin.readline().rstrip().split())

if C > B :
    ans = A // (C-B) + 1
else :
    ans = -1
print (ans)
