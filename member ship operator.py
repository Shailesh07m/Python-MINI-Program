#MemberShip Operator = It is used to whether or variable is present in sequence
#                       (String,list,tuple,set,dictonary)
Word='APPLE'
letter=input('Guess the letter of the word :')
if letter in Word:
    print(f"{letter} is in the word")
else:
    print(f"{letter} is not in the word")

Students={"Sunny",'Luffy','Zoro','Sanji'}
name=input("Enter Name for Searching :")
if name in Students:
    print(f"{name} is in the Students")
else:
    print(f"{name} is not in the Students")

Grade={"Sunny":'A','Luffy':'C','Zoro':'C','Sanji':'B'}
name1=input("Enter Name for Searching :")
if name1 in Grade:
    print(f'{name1} grade is {Grade[name1]}')
else:
    print(f'{name1} is not found in Grade')

email='mugiwara@gmail.com'
if '@' in email and '.' in email:
    print('Valid Email')
else:
    print('Invalid Email')