sum = 0
while True:
    num = int(input("enter positive integer(or enter 0 to stop): "))
    if num == 0:
        break
    elif num < 0:
        print("invalid input. Please enter a positive integer.")
        continue
    elif num % 2 == 0:
        print("skipping even numbers.")
        continue
    else:
        sum += num
        print(f"the current sum is {sum}")

print(f"the final sum is {sum}.")