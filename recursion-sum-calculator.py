# This program calculates the sume
# of all numbers entered by the user

def main():

    print("Recursion calculator")
    print("********************")
    print()

    # Get the range of numbers to be calculated
    num_items = int(input("How many numbers would you like to calculate? "))

    # Empty list to hold numbers
    list = []

    # Add numbers to the list based on
    # range set by user
    for num in range(num_items):
        num = int(input("Enter number: "))
        list.append(num)

    # range_sum function
    sum = range_sum(list, 0, num_items-1)

    # Display sum of all numbers entered
    print("The sum of the numbers you entered is:",sum)

# The range_sum uses recursion to find the
# sum of all numbers added by the user. The last variable
# is based on the range set by the user
def range_sum(items, first, last):
    if first > last:
        return 0
    else:
        return items[first] + range_sum(items, first+1, last)

main()

    


        
