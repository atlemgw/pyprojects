# Fizz Buzz

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
        
        
