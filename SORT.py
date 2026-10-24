number_ = int(input("tedadi add vared kon: "))

numbers = [0] * number_

for i in range(number_):
    numbers[i] = int(input("enter the number: "))

for i in range(number_ - 1):
    for j in range(number_ - 1 - i):
        if numbers[j] > numbers[j + 1]:
            M = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = M

print("sorted numbers:")
print(numbers)
