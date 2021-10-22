sum = 0

#100에서부터 200사이의 3의 배수의합
for i in range(100, 201):
    if( (i%3) == 0 ):
        sum += i

# ,로 나눠서 표현한다
print("sum:", sum)

