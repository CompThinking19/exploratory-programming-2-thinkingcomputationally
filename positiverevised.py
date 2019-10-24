#this function determines if an argument is a list or not
#it also iterates through the positive numbers in an argument
def positive(numbers):
    if type(numbers) != list:
        raise TypeError("Not a list")
    positive_numbers = 0
    for element in numbers:
        if element > 0:
            print_numbers += 1
    return positive_numbers

#this variable returns the positive numbers from the function
positive([1,-2,3,-4,5])

#this function should return a TypeError because the argument is a string
positive("random")
