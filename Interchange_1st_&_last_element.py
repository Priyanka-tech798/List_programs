def swapList(li):
    li[0],li[-1]=li[-1],li[0]
    return li
print("list:",swapList([12,15,17,22,67]))


outpu: [67,15,17,22,12]
