# Ask about
try:  # Try to decide what is it
    age = int(input("How years old for you?\ninput your age:"))
except:
    age = int(input("It's not a number.\nPlease input you age again:"))
age_dict = {"age": age}  # be a dict

# Other library
import time  # import about time's library
local_time = time.localtime(time.time())
local_year = int(local_time[0])

# math
birth_year = local_year - age
age_dict["birth_year"] == birth_year
now_age = local_year - birth_year
age_dict["now_age"] == now_age
adult_or_underage = ((age > 18) and ("adult",) or ("underage",))[0]
age_dict["state"] == adult_or_underage

# Result
Yes_or_no = input("Are you sure?\nPlease input Y or N .")
if Yes_or_no == "Y"
    print("You are",age_dict["state"])
elif Yes_or_no == "N"
    input("Check You input N.\nThe program wikk exit when you Click ENTER.")
else:
    input("Check You input the other letter.\nThe program wikk exit when you Click ENTER.")
