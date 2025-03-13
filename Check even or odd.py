
# x = int(input())
# if x%2 == 0:
#     print("Even")
# else:
#     print("Odd")




#use lambda with map(memory efficient):

# a = [1,2,3,4,6]
# res = map(lambda num: str(num) + "Even" if num%2 ==0 else str(num) + "Odd" , a)
# print("\n".join(res))




#using bitwise and(&) operator:
x = int(input())
if x&1 == 0:
    print("Even")
else:
    print("Odd")
