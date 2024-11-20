#Check the function the number is even or odd
def Check__even__odd(no):
    if no % 2 == 0:
        return f"'{no}' is even"
    else:
        return f"'{no}' is odd"
    
#Ask the user for a number from within the main function
def main():
    number = int(input("Enter the number: "))
    Result = Check__even__odd(number)
    print (Result)

if __name__== "__main__":
    main()
