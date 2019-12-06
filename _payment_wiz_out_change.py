# https://codeforces.com/contest/1256/problem/A

t = int(input())

for i in range(t):
    a,b,n,S = map(int,input().split())
    print( ("NO", "YES") [ (0 <= S % (n) <= b) and (a*n >= S-b) ] )
