score = int(input("Enter Your Score:"))

if score>101:
    print("Please Enter Numbers Between 0-100")
elif score>=80:
    print("A")
elif score>=70:
    print("B")
elif score>=60:
    print("C")
elif score>=50:
    print("D")
elif score>=0:
    print("F")

elif score<0:
    print("Please Enter Numbers Between 0-100")