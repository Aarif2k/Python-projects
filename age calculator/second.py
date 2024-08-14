# program to calculate age and time lived estimation
from datetime import datetime
def calculate_age(birthdate):
    today=datetime.today()
    try:
        birth_date=datetime.strptime(birthdate,'%d-%m-%Y')
        age=today.year-birth_date.year-((today.month,today.day)<(birth_date.month,birth_date.day))
        return age
    except ValueError:
        print("Enter the birthdate in the correct format(dd-mm-yyyy)")
name=input("Enter your name: ")
birthdate=input("Enter your birthdate in this format dd-mm-yyyy: ")
age=calculate_age(birthdate)
print("Your age is:",age)
days=365.25*age
minutes=525960*age
seconds=31536000*age
print(name,"you have been living for",days,'days,',minutes,'minutes and',seconds,'seconds') 
print("Thanks for using this program")