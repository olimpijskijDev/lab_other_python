#1
a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i)

#2
A = int(input())
B = int(input())
if A<B:
    for i in range(A, B+1):
        print(i)
else:
    for i in range(A, B-1, -1):
        print(i)
