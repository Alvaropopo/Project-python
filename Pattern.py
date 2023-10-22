# 1. output=1 2 3 ..... n
# n=int(input("input a number: "))
# for i in range(n):
#     print(i+1,end=" ")
# for i in range(1,n+1,1):
#     print(i,end=" ")
# 2.output=1*2*3.....n*
# for i in range(n):
#     print(i+1,end="*")
# 3.output=
#             text=alvaro
#             a
#             al
#             alv
#             alva
#             alvar
#             alvaro
# text=input("input a word: ")
# for i in range(len(text)):
#     for index in range(i+1):
#         print (text[index],end="")
#     print()

for i in range (1,11):
    print(i,end= " ")
number= int(input("input a number: "))
for i in range(1,number + 1):
    print("*"*i)