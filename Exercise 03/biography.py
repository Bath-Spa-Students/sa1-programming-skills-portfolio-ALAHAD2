#Step1:Store the information in a dictionary
Biography ={
          "Name,name:"
          "Hometown,hometown:"
          "Age,age:"
}

#Step2:Print the values on separate lines using a single print statement
print(f"Name:  {Biography ['name']}\n hometown:{Biography['hometown']}\n age:{Biography['age']}  ")

#Step3:Store the information in a use variables with appropriate data types
Name = input("enter your name: ")
Hometown = input("enter your hometown: ")

#Validate age input 
while True:
    age = int(input("enter your age:"))
    break
else:
    print("Invalid age. please enter a valid number for age ")


