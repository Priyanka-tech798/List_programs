from collections import Counter
lst=[8,6,8,10,20,8]
x=8
d = Counter(lst)
print("{} has occured {} times".format(x,d[x]))
