import datetime
import os

var1=int(input("Enter three digits. "))

var2=int(input("Enter two digits. "))

var3=int(var1 + var2)

var4=int(var1 * var2)




with open("output.txt", "a") as f:
    f.write(str(var3))
    f.write("\n")
    f.write(str(var4))
    f.write("\n")
    f.write(str(var4 + var3 - var1 * var4))
    f.write("\n")
    f.write(datetime.datetime.now().ctime())
    f.write("\n" * 2)
    
    
