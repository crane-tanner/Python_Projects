def prime_checker(number):
    isprime = True
    for i in range(2,number):
        if number % i == 0:
            isprime = False
    if isprime == False:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")
            

number = int(input("What number do you want to check?\n"))
prime_checker(number)
