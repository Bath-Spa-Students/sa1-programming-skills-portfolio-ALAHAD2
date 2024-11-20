#Define the correct password
correct_password = "12345"
max_attempt = 5

def password_entry_system():
    attempt = 0

    while attempt < max_attempt:
        password =input("Enter your password")

        if password== correct_password:
            print("password is correct.good work")
            break
        else:
            attempt += 1
            balance_attempt= max_attempt - attempt
            print(f"incorrect password{balance_attempt}.attempt balance")
    else:
        print("the authorities have been alerted.")








    
