# https://codeforces.com/contest/1256/problem/D

for i in range(int(input())):
    n,k = map(int,input().split())
    binary_string = list(input())
    ans=['1']*n
    last_zero = 0
    for i in  range (0,len(binary_string)):
        if(binary_string[i] ==  '0'):
            swaps = min(k, i - last_zero)
            k -= swaps
            ans[i-swaps]='0'
            last_zero += 1            
    print(''.join(ans))