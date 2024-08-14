print('*'*50)
print('*'*15+"College Website".center(20)+'*'*15)
print('*'*50)
      
def admin(name, subject, mark, total,reg_no):
    for n, sub, mk, t,r in zip(name, subject, mark, total,reg_no):
        print()
        print(f"Name: {n}")
        print(f"Register no.: {r}")
        for s, m in zip(sub, mk):
            print(f"{s}: {m}")
        print(f"Total: {t}")
        

def user(name, subject, mark, total,reg_no):
    while True:
        try:
            choice1 = input("Enter your name: ").lower().strip()
            if choice1 in ['gayathri', 'alisha']:
                break
            else:
                print("Please enter a valid name")
        except ValueError:
            print("Please enter a valid name")
            
    while True:
        try:
            choice2 = int(input("Enter your register number: "))
            if choice2 in [101,102]:
                break
            else:
                print("Please enter a valid register number")
        except ValueError:
            print("Please enter a valid register number")
    
    if choice1 == 'gayathri' and choice2==101:
        index1=name.index('Gayathri')
        print()
        print(f"Name: {name[index1]}")
        print(f"Register no.: {reg_no[index1]}")
        for s, m in zip(subject[index1], mark[index1]):
            print(f"{s}: {m}")
        print(f"Total: {total[index1]}")
        
  
    elif choice1 == 'alisha' and choice2==102:
        print()
        index2=name.index('Alisha')
        print(f"Name: {name[index2]}")
        print(f"Register no.: {reg_no[index2]}")
        for s, m in zip(subject[index2], mark[index2]):
            print(f"{s}: {m}")
        print(f"Total: {total[index2]}")
        
    
    else:
        print("Enter correct details.")
    
name = ["Gayathri", "Alisha"]
mark = [[85, 75, 82, 79, 94], [64, 84, 76, 80, 83]]
subject = [["Maths", "English", "Tamil", "Science", "Social"], ["Maths", "English", "Tamil", "Science", "Social"]]
mark1 = sum(mark[0])
mark2 = sum(mark[1])
total = [mark1, mark2]
reg_no=[101,102]
  
while True:
    print("Select one of the following:\n1 for Admin\n2 for User\n")
    while True:
        try:
            inp = int(input("Enter 1 or 2: "))
            if inp in [1, 2]:
                break
            else:
                print("Enter a valid choice")
        except ValueError:
            print("Please enter a valid number (1 or 2)")
    
    if inp == 1:
        admin(name, subject, mark, total,reg_no)
    else:
        user(name, subject, mark, total,reg_no)
    
    while True:
        try:
            count = input("\nDo you want to continue? Enter Y or N: ").lower()
            if count in ['y', 'n']:
                break
            else:
                print("Enter valid input")
        except ValueError:
            print("Please enter only Y or N")
    
    if count == 'y':
        continue
    else:
        print("\nThank you!")
        break
    


