def add_min_mul_div(a,b):
    return a+b, a-b, a*b, a/b

sum, min, mul, div = add_min_mul_div(3, 4)

mytuple = add_min_mul_div(3, 4)


print("sum : ", sum)
print("min : ", min)
print("mul : ", mul)
print("div : ", div)

print("mytuple : ", mytuple)

print("mytuple[0] : ", mytuple[0])
