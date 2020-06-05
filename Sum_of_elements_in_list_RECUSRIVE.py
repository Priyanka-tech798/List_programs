lst = [1,2,5,6,9,10]

def sumOfList(lst,size):
    if size == 0:
        return 0
    else:
        return lst[size-1]+sumOfList(lst,size-1)

sum = sumOfList(lst,len(lst))
print("Sum of all elements in given list is",sum)
