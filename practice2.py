
for number in range(10):
    if number == 0:
        previous_number = 0
    else:
        previous_number = number-1
    total = previous_number+number
    print(f"Current Number {number} previous number {previous_number} sum is: {total}")
    number+1
