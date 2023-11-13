score = int(input("รับค่าคะแนน:"))
    
if score>=80:
    print("A")
elif score>=70:
    print("B")
elif score>=60:
    print("C")
elif score>=50:
    print("D")
elif score>=0:
    print("คุณติด F")
else:
    print("กรุณารับป้อนข้อมูล 0-100")