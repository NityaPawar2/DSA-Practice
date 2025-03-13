def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b
a = 2
b = 3
print(swap(a,b))

#in python can be directly swapped without using third variable a,b = b,a