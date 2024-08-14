user_input=input("Enter a Phrase separated by space:")
text=user_input.split()
a=''
for i in text:
    a=a+str(i[0].upper())
print(a)