'''
Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].'''
########################################

'''
print("In the name of Allah")
#a = [12, 3, 4]
a = [-9, -2, 0, 2, 3]
print(a)
l = len(a)
#print("after sorting\n")
b = sorted(a)
c = []
print(b)

for i in range(l):
    c.append(b[i]**2)
print("after squaring and sorting the new list will be: \n")
print(sorted(c))
'''
def sqr(a):
    b = a*a
    return b
arr1 = [12, 3, 4]
l = len(arr1)
arr2 = []
arr3 = []
for i in range(l):
    num2 = sqr(arr1[i])
    arr2.append(num2)

print(f"after square root the array will be {arr2}")
#arr3 = arr2.sort()
arr2.sort()
print(f"after sorting the array will be {arr2}")






