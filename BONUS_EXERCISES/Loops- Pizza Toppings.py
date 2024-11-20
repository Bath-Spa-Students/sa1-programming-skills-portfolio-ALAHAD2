#the prompt user of pizza toppings 
def pizza_topping():
     print("welcome to pizza shop")
topping =[]

while True:
    topping=  input("Enter a pizza topping('quit' to go):")

    if topping =='quit':
       print("\nYour pizza toppings:")
    for i in topping:
         print("\n complete pizza order")
         break
    print(f"{topping} is  added to your pizza.")
else:
 print(f"Adding {topping} in  your pizza.")
 toppings.append(topping)
