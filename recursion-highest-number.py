# This program uses recursion to
# find the largest number in a list

def main():
    list = [5,6,65,80,2,102,1]

    # method for largest number
    largest = numlist(list)
    print("The largest number in the list")
    print(list,"is:",largest)
    

# The numlist function returns the largest number as
# it uses depths of recursion to return each instance.
def numlist(n):

    # Base case:
    if len(n) == 1:
        return n[0]

    # When it reaches the depths of recursion
    # replace the lower with higher number
    else:
        if n[0] > n[1]:
            n[1] = n[0]
        return numlist(n[1:])
main()
