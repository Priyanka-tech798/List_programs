import numpy
lst = [5,2,3]
result = numpy.prod(lst)
print(result)



from functools import reduce
lst = [5,2,3]
result = reduce(lambda x,y:x*y,lst)
print(result)

