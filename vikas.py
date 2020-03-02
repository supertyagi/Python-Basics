num1 = int(input("enter first no : "))
list1 = []
half1 = num1//2
print(half1)

num2 = int(input("enter second no : "))
list2 = []
half2 = num2//2
print(half2)

for first in range(1,half1+1):
    if num1%first == 0 :
        list1.append(first)
print(list1)

for second in range(1,half2+1):
    if num2%second == 0 :
        list2.append(second)
print(list2)

result = []
for element in list1:
    if element in list2:
        result.append(element)
print(max(result))