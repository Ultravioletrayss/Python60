s=input("Please enter some number")
print(s,type(s))

number1=0
number2=0
number3=0
number4=0



for t in s:
    if t.isalpha():
        print(t,"is Alpha")
    elif t.isspace():
        print(t,"is space")
    elif t.isdigit():
        print(t,"is digit")
    else:
        print(t,"is special")