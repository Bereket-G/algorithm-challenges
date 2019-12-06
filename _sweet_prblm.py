#https://codeforces.com/problemset/problem/1263/A

# t = int(input())
# while(t):
#     r,g,b = map(int,input().split())
#     cnt = min([ max([r,g,b]) ,  r + g + b  - max([r,g,b]) ]) 
#     if( r == g == b > 1):
#         cnt+=1
#     elif(r == g == max([r,g,b]) or g == b == max([r,g,b]) or r == b == max([r,g,b]) ):
#         if((r > 1 or g > 1 or b > 1) and max([r,g,b]) > 2):
#             cnt +=1
#     print (str (cnt) )
#     t-=1


for i in range(int(input())):
	a = sorted([int(i) for i in input().split()])
	print(min(a[0]+a[1], sum(a)//2))