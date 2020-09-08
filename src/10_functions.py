# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def even(n):
    if (n % 2) == 0:
        return True
    else:
        return False

num = 2
print(even(num))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def evenPrint(n):
    if (n % 2) == 0:
        return print("Even!")
    else:
        return print("Odd!")

print(evenPrint(num))


##Find a prime number 
num = input("Enter a number: ")
num = int(num)

