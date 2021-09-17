n = int(input("C = "))
if n//1 != n:
    raise TypeError("c must be an integer.")

# a, b, i = 1, n, 0
a=1
b=n
i=1
# print("a = ", a)
# print("b = ", b)
while a < b:
    i += 1
    if n % i == 0:
        a = i
        b = n//a
    
print(b, a)