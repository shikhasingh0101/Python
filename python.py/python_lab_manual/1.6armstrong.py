def is_armstrong_number(number):
    original_number = number
    n = 0
    result = 0

   
    while original_number != 0:
        original_number //= 10
        n += 1

    original_number = number

   
    while original_number != 0:
        remainder = original_number % 10
        result += remainder ** n
        original_number //= 10

   
    if result == number:
        return True
    else:
        return False


number = int(input("Enter an integer: "))

if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
