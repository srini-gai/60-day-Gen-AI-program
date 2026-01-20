
#score=int(input("Enter a exam mark"))
'''
if score >=90:
    print("A+")
elif score >80:
    print("B")
elif score >=70:
    prinnt("C")
else:
    print("FAIL")
'''

age = int(input("Enter your Age: "))

Pro = input("Enter your Sub Plan")
   

if age >= 18:
    if Pro:
        print("Full Access")
    else:
        print("Learn Mode")
else:
    print("Junior level not allowed")

Status = "Adult" if age >=18 else "minor"
print(Status)
    
