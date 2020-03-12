#the no is composite then print yes otherwise no
num = int(input())
if num > 1 :
    for i in range(2, num) :
        if (num % i) == 0 :
            print("yes")
            break
    else :
        print("no")
elif num == 0 or 1 :
    print(num, "is a neither prime NOR composite number")
else:
    print("yes")
 
