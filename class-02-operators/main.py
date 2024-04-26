import math

num1 = 2
num2 = 3

# arithmetic

print(num1 + num2)
print(num1 - num2) 
print(num1 * num2)
print(num1 / num2)
print(num1 ** num2)
print(num1 % num2)

print(pow(num1, num2))
print(round(1.5))
print(math.ceil(1.4))
print(math.floor(1.9))

# assignment
num = 2
# num = num + 1
num += 1
num -= 1
num *= 1
num /= 1
num %= 1
num **= 1

print(num)

# Comparison

print(2 == 2)
print(2 == 3)
print(2 != 3)
print(2 != 2)
print(2 > 3)
print(2 < 3)
print(2 <= 3)
print(3 >= 3)
print(1 == "1")

# Logical
# And
print(True and True)
print(True and False)
print(False and True)
print(True and False)

# Or
print(True or True)
print(True or False)
print(False or True)
print(True or False)

# Not
print(not False)
print(not True)

print(2 == 2 and 3 == 3)
print(2 != 2 and 3 == 3)
print(2 != 2 or 3 == 3)
print(2 != 2 or not 3 == 3)