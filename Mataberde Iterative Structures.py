age = int(input("Enter your age: "))
sum_of_numbers = 0
for number in range(1,age + 1):
    sum_of_numbers += number

print("The sum of all numbers from 1 to",age,"is:",sum_of_numbers)
