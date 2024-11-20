# Step1:create a dictionary for the day in the each month
month_day = {
    1:31, # january
    2:28, # february(it will adjused for leap year)
    3:31, # march
    4:30, # april
    5:31, # may
    6:30, # june
    7:31, # july
    8:31, # august
    9:30, # september
    10:31, # october
    11:30, # november
    12:31, # december
}
def is_leap_year(year):
    """Return True if the year is leap year,
    true or false otherwise"""
    if (year% 4==0 and year% 100 !=0 ) or (year % 400 ==0):
        return True
    return False

# step2:Ask the user to input the month number.
month  = int(input ("enter the month number(1-12):"))

# check if the month number is valid
if 1 <= month <=12:
  
#Step3:check for the february and handle leap
  if month ==2:
     year = int(input("enter the year to check for leap year:"))
     if is_leap_year(year):
        print(f"february{year}has 29 days")
     else:
        print(f"february {year}has 28 days")
  else:
    print(f"the month {month}has {'month__days'[month]}") 
else:
    print ("invalid month number.please enter a number between 1 and 2 ")
 

 


          
    

