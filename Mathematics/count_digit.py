# num = int(input("enter a number to count digits:"))
# count = 0
# while num!=0 :
#     digit = num % 10
#     count += 1
#     num = num // 10
# print("number of digits :", count)

num = int(input("enter number"))
count = 0
while num > 0:
    num = num // 10
    count = count +1
print("count of digits:",count)