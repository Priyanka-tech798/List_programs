lst=[10,20,40,50,80,30,105]
mx = max(lst[0],lst[1])
secmax = min(lst[0],lst[1])
for i in range(2,len(lst)):
    if lst[i]>mx:
        secmax=mx
        mx=lst[i]
    elif lst[i]>secmax and mx!=lst[i]:
        secmax = lst[i]
    else:
        if secmax == mx:
            secmax = lst[i]
print("Second highest number is ",secmax)            
