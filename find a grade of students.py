a=float(input("Enter your percentage :"))
#here we can access grade of students
if(a>90 and a<=100):
    print("grade : A+")
elif(a>80 and a<=90):
    print('grade : A')
elif(a>70 and a<=80):
    print("grade : B")   
elif(a>60 and a<=70):
    print("grade : C")
elif(a>50 and a<=60):
    print("grade :D")
elif(a>33 and a<=50):
    print("grade : E")
else:
    print("grade : F")