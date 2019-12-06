# https://codeforces.com/problemset/problem/1257/A

t = int(input())
while(t):
    n,x,a,b = map(int,input().split())
    if(abs(a-b) == (n-1) or x >= (n-abs(a-b))):
        print(n-1)
    else:
        print(x+abs(a-b))    
    t-=1
