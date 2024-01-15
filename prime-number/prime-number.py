user_input = int(input("Insert number for check if the number is 'prime number'.\nYour input number: "))

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"The number {number} is prime number")
    else:
        print(f"The number {number} is not prime number")

prime_checker(user_input)
