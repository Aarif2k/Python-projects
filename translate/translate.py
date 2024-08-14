from googletrans import Translator      # pip install googletrans == 3.1.0a0

t = Translator()

text = input("Enter the text: ")

trans = t.translate(text,dest='ta')

print(trans.text)

