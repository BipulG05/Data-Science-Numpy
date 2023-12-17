n=int(input())
h=input()
h=h.split(' ')
for i in range(0,n//2):
    if h[i]==h[i+1]:
        p=1
    else:
        p=0
print(p)