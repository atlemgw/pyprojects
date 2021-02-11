# Fizz Buzz

# Version 1 as a function
def fizzbuzz(z):
    # Loop
    for n in range(1, z + 1):
        # Fizz Buzz
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
            
        # Fizz
        elif n % 3 == 0:
            print("Fizz")
            
        # Buzz
        elif n % 5 == 0:
            print("Buzz")

        # Number
        else:
            print(n)

fizzbuzz(100)
        
# Version 2        
print("Version 2")
for tal in range(1, 101):
    fizzbuzz = ''

    if tal % 3 == 0:
        fizzbuzz = "Fizz"

    if tal % 5 == 0:
        fizzbuzz += "Buzz"

    print(fizzbuzz or tal)

# Version 3
print()
print("Version very simple!!")
for tal in range(1, 101):
    print("Fizz" * (tal % 3 == 0) + (tal % 5 == 0) * "Buzz" or tal)
