import time
import os





def my_counter() :

    if time.strftime("%H:%M:%S:%p") == "10:00:01:AM"  :
        
        
        # open both files 
        with open('log.txt','r') as firstfile, open('output.txt','a') as secondfile: 
      
            # read content from first file 
            for line in firstfile: 
               
                     # append content to second file 
                     secondfile.write(line)
                     time.sleep(2)
               

while 1 == 1 :
    my_counter()







